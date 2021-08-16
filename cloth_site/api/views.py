from datetime import date
from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from socket import socket
from django.http import JsonResponse
from api.serializers import TaskSerializer , viewSolds_serializer , SOLD_product_Serializer , createSolds_serializer , productsSerializer , viewProfit_serializer
from products.models import sold_products , products , Task , Profit
from products.views import solds


@api_view(['GET'])
def apiOverview(request):
    
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/create_sold_product/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        }
    

    return Response(api_urls)

@api_view(['GET'])
def sold_products_Api(request):
    all = sold_products.objects.all().order_by('-id')
    serializer = SOLD_product_Serializer(all, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_sold_product(request):
    print(request.data)

    Data = solds(request)
    serializer = createSolds_serializer(data=Data)
    if serializer.is_valid():
        print("valid and done ")
        serializer.save() 
    else : print ("not valid")
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    print(request.POST)
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        print ("valid and done")
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def viewTasks(request) :
    all =Task.objects.all()
    serializer = TaskSerializer(all, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def view_solds(request):
    all_products = sold_products.objects.all( ).order_by('-id')
    JsonData = viewSolds_serializer(all_products, many=True)
    return Response(JsonData.data)


@api_view(('GET',))
def view_products(request):
    all_products = products.objects.all()
    JsonData = productsSerializer(all_products, many=True)
    return Response(JsonData.data)


@api_view(('GET',))
def view_profit(request):
    all_products = Profit.objects.all()
    JsonData = viewProfit_serializer(all_products, many=True)
    return Response(JsonData.data)
