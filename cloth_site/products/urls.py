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
    path ('view_solds_page/' , views.view_solds_page , name= "view_solds_page"),
    path ('view_profit/' , views.view_profit , name= "view_profit"),
    path('view_currrent_product' , views.view_current_products , name ="view_currrent_product" ),
    path('admin/', admin.site.urls),
    path('api/' , views.api_overview , name = 'api')

]