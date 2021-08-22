from django.db import models

class products (models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True ,unique=True)
    name = models.CharField(max_length=10000 , null= True , blank= True , default="" )
    sell_price = models.DecimalField(max_digits=100, decimal_places=2 , null= True , blank= True ,  default= 0 )
    buy_price = models.DecimalField(max_digits=100, decimal_places=2, null= True , blank= True ,  default=0 )
    num_of_items = models.DecimalField(max_digits=100, decimal_places=0 , null= True , blank= True)
    factory_name= models.CharField(max_length=1000 , default="" , null= True , blank= True )
    
    def __str__(self):
        return self.product_id 


class products_inTheInVentory (models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True ,unique=True)
    name = models.CharField(max_length=10000 , null= True , blank= True , default="" )
    sell_price = models.DecimalField(max_digits=1000, decimal_places=2 , null= True , blank= True ,  default= 0 )
    buy_price = models.DecimalField(max_digits=1000, decimal_places=2, null= True , blank= True ,  default=0 )
    num_of_items = models.DecimalField(max_digits=1000, decimal_places=0 , null= True , blank= True)
    factory_name= models.CharField(max_length=1000 , default="" , null= True , blank= True )
    


class sold_products(models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True )
    sold_date = models.CharField(max_length=1000 , null= True , blank= True )
    year_month_day_solds = models.CharField(max_length=1000 , null= True , blank= True )
    discounts = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )
    price = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )
    name = models.CharField(max_length=10000 , null= True , blank= True )
    sell_price = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )



class Profit(models.Model):
    profit = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )
    Date = models.CharField(default="" , max_length=10)




class Returns_products(models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True )
    discounts = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )
    Date = models.CharField(max_length=1000 , null= True , blank= True )
    product_name = models.CharField(max_length=1000 , null= True , blank= True )

class bills(models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True )
    name = models.CharField(max_length=1000 , null= True , blank= True )
    sell_price = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True ) 
    user_paied = models.DecimalField(max_digits=19, decimal_places=2, null= True , blank= True )
    the_rest_of_money  = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )
    discounts = models.DecimalField(max_digits=19, decimal_places=2 , null= True , blank= True )
    

class Task(models.Model):
    Customer_name = models.CharField(max_length=200)
    product_id =  models.CharField(max_length=1000 , null= True , blank= True )
    product_name =  models.CharField(max_length=1000 , null= True , blank= True )
    Date = models.CharField(max_length=1000 , null= True , blank= True )

class customer_note(models.Model):
    Customer_name = models.CharField(max_length=200)
    product_id =  models.CharField(max_length=1000 , null= True , blank= True )
    product_name =  models.CharField(max_length=1000 , null= True , blank= True )
    Date = models.CharField(max_length=1000 , null= True , blank= True )
