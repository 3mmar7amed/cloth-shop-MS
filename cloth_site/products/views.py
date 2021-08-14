from functools import partial
from django.http import HttpResponseRedirect
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from rest_framework.exceptions import ErrorDetail
from products.Forms import  sellForm , insertProductForm
from products.models import products , sold_products , Profit
from django.utils import timezone
import datetime 
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from socket import socket
from .jsonReturn import productsSerializer , SOLD_product_Serializer , viewSolds_serializer, viewProfit_serializer



def ProductInfo(request):

    if request.method == 'POST':
        try:
            print("pooooooooooooooooooooost")
            id = request.POST.get('product_id')
            name = request.POST.get('name')
            sell_price = request.POST.get('sell_price')
            buy_price = request.POST.get('buy_price')
            factory = request.POST.get('factory_name')
            product_count = request.POST.get('num_of_items')
            q = products(product_id = id , name = name  ,sell_price = sell_price , buy_price = buy_price , num_of_items = product_count , factory_name = factory)
            q.save()

            messages.success(request, 'تم إضـافة البضاعة بنجاح  ')
        except:
            messages.success(request, 'لم يتم اضافة البضاعة ، قد يكون  كود المنتج مكرر ، حاول استخدام كود خاص بكل منتج ')
        
        return redirect('insertProduct')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = insertProductForm()
    return render(request, 'data_form.html', {'form': form} )



@api_view(('GET',))
def api_overview(request):

    api_url = {
        "sell" : '/sell/<str:pk>' ,
        "view_products": '/view/' ,
        'view_solds' : '/view_solds',
    }

    return Response(api_url)

@api_view(('GET','POST'))
def solds(request ):
    
    if request.method == 'POST':

        form = sellForm(request.POST)
        if form.is_valid():
            pay = form.cleaned_data.get('pay')
            id = form.cleaned_data.get('product_id')
            print(id + "here is the id ")
            product_info = products.objects.get(product_id = id)
            product_info.num_of_items -= 1
            product_info.save()
            disc = product_info.sell_price - pay
            now = datetime.datetime.now()
            data = {
                "sold_date" : now , 
                "price" : pay , 
                "prodcut_info" : product_info,
                "discounts" : disc
            }
            serializer =viewSolds_serializer(data = data)
            serializer.save() 
            

            calculate_profit(product_info.buy_price , pay )
            return Response(serializer.data)
            
    else:
        form = sellForm()
        
    return render(request, 'sell.html', {'form': form} )



def calculate_profit(buy_price , pay ) :
    profit = pay - buy_price
    today = datetime.datetime.now()
    month = today.month
    year = today.year
    str = month +"-"+year
    print (str)
    try:
        q = Profit.objects.get(Date = str)
        q.profit += profit
    except:
        q = Profit(profit = profit , Date = str)
       
    q.save()

@api_view(('GET',))
def view_products(request):
    all_products = products.objects.all()
    JsonData = productsSerializer(all_products, many=True)
    return Response(JsonData.data)




@api_view(('GET',))
def view_solds(request):
    all_products = sold_products.objects.all( )
    JsonData = viewSolds_serializer(all_products, many=True)
    return Response(JsonData.data)


@api_view(('GET',))
def view_profit(request):
    all_products = Profit.objects.all()
    JsonData = viewProfit_serializer(all_products, many=True)
    return Response(JsonData.data)



def barcode(request):
    return render (request , "barcode.html" )

def Print_barcode(request):
    return render (request , "print.html" )





