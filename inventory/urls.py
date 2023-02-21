from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views


from rest_framework.routers import DefaultRouter


'''
check for default router from documentation
'''

urlpatterns = [
    path('api/inventories/', views.ListInventoriesMixins.as_view(), name='inventories'),
    path('api/inventory/<int:pk>/',
         views.DetailedInventoryMixins.as_view(), name='inventory_detail'),
    path('inventory/', views.inventories, name='inventories_view'),
    path('inventory/<int:pk>', views.ViewInventoryDetail,
         name='inventory_detail_view')
]

urlpatterns = format_suffix_patterns(urlpatterns)
