# Generated by Django 3.1.5 on 2021-03-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0009_auto_20210328_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(help_text='Similar to stock_item_code above', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='updateprice',
            name='item_code',
            field=models.CharField(help_text='Similar to stock_item_code above', max_length=200, null=True),
        ),
    ]