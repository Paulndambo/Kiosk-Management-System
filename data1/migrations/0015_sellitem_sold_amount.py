# Generated by Django 3.1.5 on 2021-03-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0014_sellitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellitem',
            name='sold_amount',
            field=models.IntegerField(default=0),
        ),
    ]
