# Generated by Django 3.1.5 on 2021-04-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0036_auto_20210401_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellitem',
            name='selling_price',
            field=models.FloatField(default=0),
        ),
    ]
