# Generated by Django 3.1.5 on 2021-03-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0024_restock'),
    ]

    operations = [
        migrations.AddField(
            model_name='restock',
            name='item_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
