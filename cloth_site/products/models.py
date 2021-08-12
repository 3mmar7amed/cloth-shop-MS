from django.db import models

class products (models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True)
    name = models.CharField(max_length=10000 , null= True , blank= True )
    sell_price = models.DecimalField(max_digits=19, decimal_places=10 , null= True , blank= True )
    buy_price = models.DecimalField(max_digits=19, decimal_places=10 , null= True , blank= True )
    num_of_items = models.DecimalField(max_digits=19, decimal_places=10 , null= True , blank= True)
    factory_name= models.CharField(max_length=1000 , default="" , null= True , blank= True)

