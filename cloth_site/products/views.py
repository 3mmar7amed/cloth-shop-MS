from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib import messages
from products.Forms import insertProductForm
from products.models import products



def ProductInfo(request):
    form = insertProductForm()
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        print("post method")
        id = request.POST.get('product_id')
        name = request.POST.get('name')
        sell_price = request.POST.get('sell_price')
        buy_price = request.POST.get('buy_price')
        factory = request.POST.get('factory_name')
        product_count = request.POST.get('num_of_items')
    
        messages.success(request, 'تم إضـافة البضاعة بنجاح  ')
        query = products(product_id= id , name = name  ,sell_price = sell_price  , buy_price=buy_price , factory_name=factory , num_of_items = product_count)
        query.save()
        return redirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = insertProductForm()

    return render(request, 'data_form.html', {'form': form} )