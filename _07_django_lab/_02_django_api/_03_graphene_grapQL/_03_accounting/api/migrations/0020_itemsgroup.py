# Generated by Django 3.1.2 on 2020-10-29 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201029_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('SKU', models.CharField(blank=True, max_length=255, null=True)),
                ('volume_cbm', models.FloatField(default=0)),
                ('upc_no', models.CharField(blank=True, max_length=100, null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=100, null=True)),
                ('warranty_month', models.IntegerField(blank=True, null=True)),
                ('tags', models.CharField(max_length=100)),
                ('account_name_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.accountname')),
                ('item_brand_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.itembrands')),
                ('item_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.itemtype')),
                ('supplier_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.supplier')),
            ],
        ),
    ]
