# Generated by Django 3.1.2 on 2020-11-03 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20201102_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountname',
            name='account_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.accounttype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='head_of_accounts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.head_of_accounts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientadditionalcontacts',
            name='client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.clients'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientaddress',
            name='client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.clients'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientaddress',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.clients'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='currency_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.currency'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='pay_term_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.paymentterms'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='payment_method_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.paymentmethods'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryadjustment',
            name='acc_name_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.accountname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryadjustmentitems',
            name='inventory_adjustment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.inventoryadjustment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemgroupmapping',
            name='item_group_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itemsgroup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemgroupmapping',
            name='item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.items'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='account_name_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.accountname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='item_brand_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itembrands'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='item_category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itemcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='item_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itemtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.supplier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemsgroup',
            name='account_name_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.accountname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemsgroup',
            name='item_brand_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itembrands'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemsgroup',
            name='item_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itemtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemsgroup',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.supplier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemstorage',
            name='storage_location_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.storagelocation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemstoragemapping',
            name='item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.items'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemstoragemapping',
            name='item_storage_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.itemstorage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storagelocation',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier_additional_contacts',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.supplier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplieraddress',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplieraddress',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.supplier'),
        ),
        migrations.AlterField(
            model_name='supplierdetails',
            name='currency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.currency'),
        ),
        migrations.AlterField(
            model_name='supplierdetails',
            name='pay_term_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.paymentterms'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplierdetails',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.supplier'),
            preserve_default=False,
        ),
    ]
