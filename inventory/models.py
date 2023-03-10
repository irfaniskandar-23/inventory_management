from django.db import models

# Create your models here.


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')

    class Meta:

        db_table = 'suppliers'

    def __str__(self):
        return '%s' % (self.name)


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    note = models.TextField()
    stock = models.IntegerField(default=1)
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE)  # Foreign Key relationship with supplier

    class Meta:
        db_table = 'inventories'

    def __str__(self):
        return '%s' % (self.name)
