# Generated by Django 3.1.5 on 2021-03-28 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0003_updateprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateprice',
            name='stock_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data1.stock', unique=True),
        ),
    ]
