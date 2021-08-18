import datetime 
from datetime import date
import re
from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from socket import socket
from django.http import JsonResponse
from api.serializers import viewSolds_serializer , returns_serializer , viewDailySolds_serializer  , createSolds_serializer , productsSerializer , viewProfit_serializer
from products.models import sold_products , products  , Profit , Returns_products
from products.views import solds , returns



@api_view(['POST'])
def create_sold_product(request):

    Data = solds(request)
    print(Data)
    serializer = createSolds_serializer(data=Data)
    if serializer.is_valid():
        print("valid and done ")
        serializer.save() 
    else : print ("not valid")
    return Response(serializer.data)


@api_view(('GET',))
def view_solds(request):
    all_products = sold_products.objects.all().order_by('-id')
    JsonData = viewSolds_serializer(all_products, many=True)
    return Response(JsonData.data)

@api_view(('GET',))
def view_daily_solds(request):
    today = datetime.datetime.now()
    Y_M_D_solds = today.strftime(("%d-%m-%Y"))
    all_products = sold_products.objects.filter(year_month_day_solds =Y_M_D_solds ).order_by('-id')
    JsonData = viewDailySolds_serializer(all_products, many=True)
    return Response(JsonData.data)

@api_view(('GET',))
def view_products(request):
    all_products = products.objects.all().order_by('-id')
    JsonData = productsSerializer(all_products, many=True)
    return Response(JsonData.data)


@api_view(('GET',))
def view_profit(request):
    all_products = Profit.objects.all()
    JsonData = viewProfit_serializer(all_products, many=True)
    return Response(JsonData.data)


@api_view(['POST'])
def reduce_profit_by_discount(request):

    discount = request.data.get('discounts')
    q = Profit.objects.filter().last()
    try:
        new_profit = q.profit - int(discount)
    except:
        new_profit = q.profit
    q.profit = new_profit
    q.save()
    return Response()


@api_view(['POST' , 'GET'])
def returns_products(request):
    if request.method == 'POST':
        id = request.data.get('product_id')
        discount = request.data.get('discount')
        returns(id , discount)
        print(id)
        product_name =products.objects.get(product_id  = id).name
        today = datetime.datetime.now()
        date = today.strftime(("%d-%m-%Y    %H:%M:%S"))
        data = {
            "discount" : discount , 
            "product_id" : id , 
            "date" : date , 
            "name" : product_name
        }
        return Response(data = data)
    else :
        all_products = Returns_products.objects.all()
        JsonData = returns_serializer(all_products, many=True)
        return Response(JsonData.data)
    
