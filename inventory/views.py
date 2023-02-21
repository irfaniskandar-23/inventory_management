from django.shortcuts import render
from django.http import Http404
from inventory.models import Supplier, Inventory
from inventory.serializers import supplierSerializer, inventorySerializer


from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
import requests


class ListInventoriesMixins(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Inventory.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class DetailedInventoryMixins(mixins.RetrieveModelMixin,
                              generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


def inventories(request):
    
    inventory = requests.get('http://127.0.0.1:8000/api/inventories/').json()
    return render(request, 'inventory.html', {'response': inventory})


def ViewInventoryDetail(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/inventory/{pk}')
    data = response.json()

    if response.status_code == 200:
        return render(request, 'inventory_detail.html', {'response': data}, status=status.HTTP_200_OK)

    else:
        raise Http404
