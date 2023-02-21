from rest_framework import serializers
from inventory.models import Supplier, Inventory


class supplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


class inventorySerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()

    class Meta:
        model = Inventory
        fields = '__all__'