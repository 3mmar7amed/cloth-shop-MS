from django.contrib import admin
from products import  views
from django.urls import include, path


urlpatterns = [
    path('' , views.solds , name = "sell") , 
    path('view/' , views.view_products) ,
    path ('insertProduct/' , views.ProductInfo , name= "insertProduct"),
    path('admin/', admin.site.urls),

]