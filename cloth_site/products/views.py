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
from api.serializers import productsSerializer , SOLD_product_Serializer , viewSolds_serializer, viewProfit_serializer



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





def solds(request):
 
    if request.method == 'POST':
        id = request.data.get('product_id')
        disc = request.data.get('discounts')
        pay = request.data.get('pay')
        print(type(request.data))
        product_info = products.objects.get(product_id = id)
        product_info.num_of_items -= 1
        product_info.save()
        
        
        try:
            price_after_discount = (product_info.sell_price) - int(disc)
        except:  price_after_discount = (product_info.sell_price) 
        
            
        data = {
                "product_id" : id ,
                "name" : product_info.name , 
                "sell_price" : product_info.sell_price , 
                "discounts" : disc ,
                "price" : price_after_discount,

            }
        
        #calculate_profit(product_info.buy_price , what_he_paid )
        return (data)     
            
    else:
        form = sellForm()
    return render(request, 'sell2.html', {'form': form} )




def calculate_profit(buy_price , pay ) :
    profit = pay - buy_price
    today = datetime.datetime.now()
    month = today.month
    year = today.year
##############E#######W## wait until el5awal make submit button ####################################################################################
    date = month +"-"+year
    print (date)
    try:
        q = Profit.objects.get(Date = date)
        q.profit += profit
    except:
        q = Profit(profit = profit , Date = date)
       
    q.save()


def view_current_products(request):
    return render (request , "view_products.html")

def view_solds_page(request):
    return render(request , "view_solds.html")






def barcode(request):
    return render (request , "barcode.html" )

def Print_barcode(request):
    return render (request , "print.html" )





