import datetime 
from datetime import date
import re
from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from socket import socket
from django.http import JsonResponse
from api.serializers import viewSolds_serializer ,bills_serializer,  returns_serializer , viewDailySolds_serializer  , createSolds_serializer , productsSerializer , viewProfit_serializer
from products.models import sold_products , products  , Profit , Returns_products , bills
from products.views import solds , returns



@api_view(['POST'])
def create_sold_product(request):

    Data = solds(request)
    print(Data)
    serializer = createSolds_serializer(data=Data)
    if serializer.is_valid():
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
    


@api_view(['DELETE'])
def productDelete(request, pk):
    PK = str(pk)
    try:
        task = products.objects.get(product_id=PK)
        task.delete()
    except:
        return Response('Item wasnot deleted!')

    return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def billsDelete(request):

        task = bills.objects.all()
        task.delete()
        print("delete is done ")
        return Response('Item succsesfully delete!')



@api_view(['POST' , 'GET'])
def putSoldsInBill(request):

    if request.method == 'POST':
            print("it's poooooooost method")
            print("iam here ")

            try:
                id = request.data.get('product_id')
                print(id)
                ID = str(id)
                q = products.objects.get(product_id = ID)
                name = q.name
                price = q.sell_price
                DATA = {
                    "product_id" : ID , 
                    "name" : name , 
                    "sell_price" : price ,
                }
            except:
                user_paied = request.data.get('user_paied')
                over_All_price = request.data.get('over_All_price')
                discounts = request.data.get('discounts')
                the_rest_of_money = request.data.get('the_rest_of_money')
                DATA = {
                    "the_rest_of_money" : the_rest_of_money ,
                    "discounts" :discounts ,
                    "over_All_price" :over_All_price , 
                    "user_paied" : user_paied ,
                }

            serializer = bills_serializer(data=DATA)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
    else :
        all_products = bills.objects.all()
        JsonData = bills_serializer(all_products, many=True)
        return Response(JsonData.data)
    

    
   
