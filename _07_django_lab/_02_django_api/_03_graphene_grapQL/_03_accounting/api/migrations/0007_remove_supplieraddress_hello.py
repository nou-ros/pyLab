# Generated by Django 3.1.2 on 2020-10-21 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_supplieraddress_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplieraddress',
            name='hello',
        ),
    ]
