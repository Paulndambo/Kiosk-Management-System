# Generated by Django 3.1.5 on 2021-04-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0039_auto_20210401_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytotalsales',
            name='sales_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
