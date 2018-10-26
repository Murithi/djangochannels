from channels.routing import route
from example.consumers import ws_connect, ws_disconnect, ws_message, received_payment


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route("websocket.receive", ws_message),
    route('received-payment', received_payment),
]
