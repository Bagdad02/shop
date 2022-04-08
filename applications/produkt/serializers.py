from rest_framework import serializers

from applications.produkt.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','owner', 'name', 'description', 'price', 'category', 'images' )