# Generated by Django 3.1.5 on 2021-04-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0045_sellitem_date_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='date_sold',
            field=models.DateField(auto_now_add=True),
        ),
    ]