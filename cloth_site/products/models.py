from django.db import models

class products (models.Model):
    product_id = models.CharField(max_length=1000)
    name = models.CharField(max_length=10000)
    sell_price = models.DecimalField(max_digits=19, decimal_places=10)
    buy_price = models.DecimalField(max_digits=19, decimal_places=10)
    num_of_items = models.DecimalField(max_digits=19, decimal_places=10)

