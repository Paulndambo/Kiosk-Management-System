# Generated by Django 3.1.5 on 2021-04-01 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0037_sellitem_selling_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailytotalsales',
            options={'verbose_name_plural': 'Daily Total Sales'},
        ),
        migrations.AlterModelOptions(
            name='sellitem',
            options={'verbose_name_plural': 'Sold Items'},
        ),
    ]
