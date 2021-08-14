from rest_framework import serializers
from products.models import products , sold_products  , Profit

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'


class SOLD_product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('name' , 'price')

class viewSolds_serializer(serializers.ModelSerializer):
    class Meta:
        model = sold_products
        fields = '__all__'



class viewProfit_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = '__all__'