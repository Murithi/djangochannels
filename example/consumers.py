import json
from channels import Group

import threading
import random


def received_payment(message):
    print(message['status'])

    Group('safcom').send({'text': message['status']})


def sendmsg(msg):
    Group('safcom').send({'text': msg})


t = 0


def periodic():
    global t
    n = random.randint(100, 200)
    # sendmsg(str(n))
    t = threading.Timer(5, periodic)
    t.start()


def ws_message(message):
    global t
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print(message.content['text'])
    if (message.content['text'] == 'start'):
        periodic()
    else:
        t.cancel()
   # message.reply_channel.send({'text':'200'})


def ws_connect(message):
    Group('safcom').add(message.reply_channel)
    Group('safcom').send({'text': 'Processing Payment'})


def ws_disconnect(message):
    Group('safcom').send({'text': 'disconnected'})
    Group('safcom').discard(message.reply_channel)
