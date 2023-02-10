from django.db import models

# Create your models here.


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')

    class Meta:
        verbose_name_plural = 'Supppliers'

    def __str__(self):
        return self.name


class inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(
        Supplier, default=1, verbose_name='Supplier', on_delete=models.CASCADE)  # Foregin Key relationship with supplier

    class Meta:
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return self.name
