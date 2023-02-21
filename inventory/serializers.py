from rest_framework import serializers
from inventory.models import Supplier, Inventory


class supplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('name')


class inventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('name', 'description', 'note',
                  'stock', 'availability', 'supplier')
        lookup_field = 'supplier'
