from datetime import datetime
from django.db import models

class products (models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True ,unique=True)
    name = models.CharField(max_length=10000 , null= True , blank= True )
    sell_price = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    buy_price = models.DecimalField(max_digits=19, decimal_places=3, null= True , blank= True )
    num_of_items = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True)
    factory_name= models.CharField(max_length=1000 , default="" , null= True , blank= True)
    
    def __str__(self):
        return self.product_id 



class sold_products(models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True )
    sold_date = models.DateTimeField(auto_now= datetime.day)
    discounts = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    price = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    name = models.CharField(max_length=10000 , null= True , blank= True )
    sell_price = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )



class Profit(models.Model):
    profit = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    Date = models.CharField(default="" , max_length=10)

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title