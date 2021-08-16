from django.contrib import admin
from api import  views
from django.urls import  path


urlpatterns = [
    
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-list/', views.viewTasks, name="task-list"),
    path('sold_products_Api/', views.sold_products_Api, name="sold_products_Api"),
    path('create_sold_product/' , views.create_sold_product , name ="create_sold_product" ),
    path('view_sold_product/' , views.view_solds , name ="view_sold_product" ),
    path('view_profit/' , views.view_profit , name ="view_profit" ),
    path('reduce_profit_by_discount/' , views.reduce_profit_by_discount , name ="reduce_profit_by_discount" ),

    path('view/' , views.view_products , name = "view") ,
]
