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
        id = request.POST.get('product_id')
        name = request.POST.get('name')
        sell_price = request.POST.get('sell_price')
        buy_price = request.POST.get('buy_price')
        factory = request.POST.get('factory_name')
        product_count = request.POST.get('num_of_items')
        print(product_count)
        try:
                already_exsit = products.objects.get(product_id = id)
                if name is '':
                    already_exsit.num_of_items +=int(product_count)
                    already_exsit.save()
                    
                    messages.success(request, 'تم زيادة عدد البضاعة بنجاح  ')
                else:
                    messages.success(request, 'لم يتم اضافة البضاعة ، قد يكون  كود المنتج مكرر ، حاول استخدام كود خاص بكل منتج ')
        except:
            q = products(product_id = id , name = name  ,sell_price = sell_price , buy_price = buy_price , num_of_items = product_count , factory_name = factory)
            q.save()
            messages.success(request, 'تم إضـافة البضاعة بنجاح  ')


        return redirect('insertProduct')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = insertProductForm()
    return render(request, 'data_form.html', {'form': form} )





def solds(request):
 
    if request.method == 'POST':

        id = request.data.get('product_id')
        
        product_info = products.objects.get(product_id = id)
        product_info.num_of_items -= 1
        product_info.save()
        
        today = datetime.datetime.now()
        date = today.strftime(("%d-%m-%Y    %H:%M:%S"))
        Y_M_D_solds = today.strftime(("%d-%m-%Y"))
        print( today.strftime(("%d-%m-%Y")) )
        data = {
                    "product_id" : id ,
                    "name" : product_info.name , 
                    "sell_price" : product_info.sell_price , 
                    "sold_date" : date,
                    "year_month_day_solds" : Y_M_D_solds,
                }
            
        calculate_profit(product_info.buy_price , product_info.sell_price )
        
        return data    
            
    else:
        form = sellForm()
    return render(request, 'sell2.html', {'form': form} )




def calculate_profit(buy_price , pay ) :
    profit = pay - buy_price
    today = datetime.datetime.now()
    month = today.month
    year = today.year
    date = str(month) +"-"+str(year)
    print (date)
    try:
        q = Profit.objects.get(Date = date)
        q.profit += profit
    except:
        q = Profit(profit = profit , Date = date)
       
    q.save()

def returns(id , discount):

        if(discount == ''):
            discount = 0 
        product_info = products.objects.get(product_id = id)
        product_info.num_of_items += 1
        product_info.save()
        profit = product_info.buy_price - product_info.buy_price 
        q = Profit.objects.filter().last()
        q.profit -= (profit- discount )
        q.save()

def Return_product(request):
    return render(request , "returns.html")

def view_current_products(request):
    return render (request , "view_products.html")

def view_solds_page(request):
    return render(request , "view_solds.html")


def delete_product(request):

    return render (request , "delete.html" )


def viewBills(request):
    return render (request , "bills.html" )

def barcode(request):
    return render (request , "barcode.html" )

def Print_barcode(request):
    return render (request , "print.html" )





