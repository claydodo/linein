__all__ = [
    'UserSerializer', 'TagSerializer', 'ProductSerializer', 'OrderProductEntrySerializer', 'OrderSerializerWithSave', 'OrderSerializerWithoutSave',
    'EntitySerializer',
]

from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'desc', 'tags', 'on_shelf']


class ProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductEntry
        fields = ['product', 'count']


class OrderProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductEntry
        fields = ['order', 'product', 'count']


class OrderSerializerWithSave(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'user',
            'product_entries'
        ]

    product_entries = ProductEntrySerializer(many=True)

    def create(self, validated_data):
        # This is way too complex
        product_entries_data = validated_data.pop('product_entries', [])
        order = Order.objects.create(**validated_data)
        for entry_info in product_entries_data:
            OrderProductEntry.objects.create(order=order, **entry_info)
        return order

    def update(self, instance, validated_data):
        pass


class OrderSerializerWithoutSave(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user']


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['id', 'subs']
