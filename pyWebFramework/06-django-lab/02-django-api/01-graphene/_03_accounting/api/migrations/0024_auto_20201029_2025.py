# Generated by Django 3.1.2 on 2020-10-29 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_accounttype_head_of_accounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='head_of_accounts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.head_of_accounts'),
        ),
    ]
