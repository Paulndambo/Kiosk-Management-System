# Generated by Django 3.1.5 on 2021-04-01 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0041_remove_sellitem_date_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailytotalsales',
            name='sales_date',
        ),
    ]