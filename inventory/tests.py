from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# Create your tests here.


class Inventory(APITestCase):
    def apiInventory(self):
        response = self.client.get(reverse('inventories'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
