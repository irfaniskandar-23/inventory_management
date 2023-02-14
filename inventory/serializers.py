from rest_framework import serializers
from inventory.models import Supplier, inventory


class inventorySerializer(serializers.ModelSerializer):
    # supplier_name = serializers.CharField(source='supplier.name')

    class Meta:
        model = 'Inventory'
        fields = '__all__'


class supplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Supplier'
        fields = '__all__'
