# Generated by Django 4.1.6 on 2023-02-14 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='supplier',
            new_name='supplier_id',
        ),
    ]