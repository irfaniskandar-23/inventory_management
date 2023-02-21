from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views


'''
check for default router from documentation
'''
urlpatterns = [
    path('api/inventory/', views.inventoryList.as_view(),
         name='inventories'),  # backend url

    path('api/inventory/<int:pk>',
         views.InventoryDetail.as_view(), name='inventory_detail'),

    path('inventory/', views.inventories, name='inventories_view'),

    path('inventory/<int:pk>', views.ViewInventoryDetail,
         name='inventory_detail_view')
]

urlpatterns = format_suffix_patterns(urlpatterns)
