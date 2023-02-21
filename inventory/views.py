from django.shortcuts import render
from django.http import Http404
from inventory.models import Inventory
from inventory.serializers import inventorySerializer


from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
import requests


class ListInventoriesMixins(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Inventory.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


class DetailedInventoryMixins(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              generics.GenericAPIView):

    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def inventories(request):
    response = requests.get('http://127.0.0.1:8000/api/inventory/').json()
    return render(request, 'inventory.html', {'response': response})


def ViewInventoryDetail(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/inventory/{pk}').json()
    return render(request, 'inventory_detail.html', {'response': response}, status=status.HTTP_200_OK)
