from django.db import models

class products (models.Model):
    product_id = models.CharField(max_length=1000 , null= True , blank= True ,unique=True)
    name = models.CharField(max_length=10000 , null= True , blank= True )
    sell_price = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    buy_price = models.DecimalField(max_digits=19, decimal_places=3, null= True , blank= True )
    num_of_items = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True)
    factory_name= models.CharField(max_length=1000 , default="" , null= True , blank= True)
    
    def dict(self):
        context = {
            "name" : self.name,
            "price" : self.product_id
        }
        return context 



class sold_products(models.Model):
    sold_date = models.DateTimeField()
    discounts = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    price = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    product_info = models.ForeignKey(products, on_delete=models.CASCADE)


class Profit(models.Model):
    profit = models.DecimalField(max_digits=19, decimal_places=3 , null= True , blank= True )
    Date = models.CharField(default="" , max_length=10)

