from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# Create your tests here.


class InventoryTest(APITestCase):
    def test_api_inventory(self):
        response = self.client.get(reverse("inventories"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_inventory(self):
        response = self.client.get(reverse('inventories_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_detail_inventory(self):
        url = reverse("inventory_detail_view", kwargs={"pk": 2})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
