from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from channels import Channel
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


@csrf_exempt
@api_view(['POST'])
def RecievePayment(request):
    phonenum = request.data['phonenum']
    amount = request.data['amount']
    print(phonenum, amount)
    Channel('received-payment').send({
        "status": "Transaction Successful"

    })

    return Response(status=status.HTTP_204_NO_CONTENT)
