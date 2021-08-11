from django.shortcuts import render
# Create your views here.

# insert products by the id and name 
def home (request , *args , **kwargs ):
    return render (request , "data_form.html")

