# Generated by Django 3.1.2 on 2020-10-28 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_itembrands_itemcategory_itemtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='payment_method_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.paymentmethods'),
        ),
    ]