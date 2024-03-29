# Generated by Django 3.1.2 on 2020-11-02 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_itemtransfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemstoragemapping',
            name='volume',
            field=models.CharField(default='volume-1', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ItemTransferMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('volume', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.items')),
                ('item_transfer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.itemtransfer')),
            ],
        ),
    ]
