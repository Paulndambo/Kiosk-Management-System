# Generated by Django 3.1.5 on 2021-03-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0007_auto_20210328_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='stock',
            new_name='stock_item_code',
        ),
        migrations.AddField(
            model_name='item',
            name='item_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]