# Generated by Django 3.1.5 on 2021-03-31 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0029_auto_20210331_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellitem',
            old_name='item',
            new_name='item_code',
        ),
        migrations.RenameField(
            model_name='sellitem',
            old_name='stock_item_code',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='sellitem',
            old_name='sold_amount',
            new_name='sold_quantity',
        ),
    ]
