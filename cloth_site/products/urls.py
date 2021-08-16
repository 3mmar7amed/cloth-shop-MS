from django.contrib import admin
from products import  views
from django.urls import include, path


urlpatterns = [
    path('' , views.solds , name = "sell") , 
    path('barcode/' , views.barcode , name="barcode") ,
    path('print/' , views.Print_barcode , name="print") ,
    path ('insertProduct/' , views.ProductInfo , name= "insertProduct"),
    path ('view_solds_page/' , views.view_solds_page , name= "view_solds_page"),
    path('view_currrent_product' , views.view_current_products , name ="view_currrent_product" ),
    path('admin/', admin.site.urls),
    

]