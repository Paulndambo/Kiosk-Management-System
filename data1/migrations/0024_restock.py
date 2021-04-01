# Generated by Django 3.1.5 on 2021-03-31 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0023_delete_restock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restock',
            fields=[
                ('restock_number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('item_char', models.CharField(max_length=200, null=True)),
                ('item_slug', models.SlugField(max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('stock_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data1.stock')),
            ],
        ),
    ]