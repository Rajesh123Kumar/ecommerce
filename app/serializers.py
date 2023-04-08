from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(max_length=100)
    product_price=serializers.IntegerField()
    product_quantity=serializers.IntegerField()

    class Meta:
        model=CartItem
        fields=('__all__')

