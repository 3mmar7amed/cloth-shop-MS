from django.contrib import admin
from api import  views
from django.urls import  path


urlpatterns = [
    path('view/' , views.view_products , name = "view") ,
    path('create_sold_product/' , views.create_sold_product , name ="create_sold_product" ),
    path('view_sold_product/' , views.view_solds , name ="view_sold_product" ),
    path('view_daily_solds/' , views.view_daily_solds , name ="view_daily_solds" ),
    path('view_profit/' , views.view_profit , name ="view_profit" ),
    path('reduce_profit_by_discount/' , views.reduce_profit_by_discount , name ="reduce_profit_by_discount" ),
    path('returns_products/' , views.returns_products , name ="returns_products" ),
    path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),
    path('bills/' , views.putSoldsInBill , name ="bills" ),
    path('DeleteBills/' , views.billsDelete , name ="DeleteBills" ),
]
