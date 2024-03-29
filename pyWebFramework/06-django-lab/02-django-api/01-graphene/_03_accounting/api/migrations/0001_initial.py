# Generated by Django 3.1.2 on 2020-10-19 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('corporation_no', models.CharField(blank=True, max_length=100, null=True)),
                ('salutation', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('display_name', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier_Additional_Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('salutation', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('supplier_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.supplier')),
            ],
        ),
    ]
