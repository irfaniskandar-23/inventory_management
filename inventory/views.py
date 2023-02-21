from django.shortcuts import render
from inventory.models import Supplier, Inventory
from inventory.serializers import supplierSerializer, inventorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import requests


class inventoryList(APIView):
    '''
    get list of invetorires
    '''

    def get(self, request, format=None):
        try:
            queryset = Inventory.objects.all()
            name = self.request.query_params.get('name', None)
            if name is not None:
                queryset = queryset.filter(name=name)

            serialize_inventories = inventorySerializer(queryset, many=True)
            return Response(serialize_inventories.data, status=status.HTTP_200_OK)

        except Exception as error:
            print(str(error))


class InventoryDetail(APIView):
    '''
    retrieve specific inventory item
    '''

    def get_item(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventory = self.get_item(pk)
        serializer = inventorySerializer(inventory)
        return Response(serializer.data, status=status.HTTP_200_OK)


def inventories(request):

    inventory = requests.get('http://127.0.0.1:8000/api/inventory/').json()
    return render(request, 'inventory.html', {'response': inventory})


def ViewInventoryDetail(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/inventory/{pk}')
    data = response.json()

    if response.status_code == 200:
        return render(request, 'inventory_detail.html', {'response': data}, status=status.HTTP_200_OK)

    ViewInventoryDetail()

    # else:
    #     raise Http404
