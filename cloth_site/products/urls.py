from django.contrib import admin
from products import  views
from django.urls import include, path


urlpatterns = [
    path('' , views.solds , name = "sell") , 
    path('soladsAPI/' , views.soldsAPI), 
    path('view/' , views.view_products , name = "view") ,
    path('barcode/' , views.barcode , name="barcode") ,
    path('print/' , views.Print_barcode , name="print") ,
    path ('insertProduct/' , views.ProductInfo , name= "insertProduct"),
    path ('view_solds/' , views.view_solds , name= "view_solds"),
    path ('view_profit/' , views.view_profit , name= "view_profit"),
    path ('view_priceandname/' , views.view_PriceAndName , name= "view_priceandname"),

    path('admin/', admin.site.urls),
    path('api/' , views.api_overview , name = 'api')

]