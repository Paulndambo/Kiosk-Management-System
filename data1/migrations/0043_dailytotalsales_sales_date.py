# Generated by Django 3.1.5 on 2021-04-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0042_remove_dailytotalsales_sales_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytotalsales',
            name='sales_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
