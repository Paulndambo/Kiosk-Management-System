# Generated by Django 3.1.5 on 2021-03-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0008_auto_20210328_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updateprice',
            old_name='stock',
            new_name='stock_item_code',
        ),
        migrations.AddField(
            model_name='updateprice',
            name='item_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
