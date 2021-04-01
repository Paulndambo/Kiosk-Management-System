# Generated by Django 3.1.5 on 2021-03-28 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=200, unique=True)),
                ('item_name', models.CharField(max_length=200)),
                ('buying_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('available_items', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UpdatePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buying_price', models.FloatField(default=0)),
                ('selling_price', models.FloatField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data1.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='stock_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data1.stock'),
        ),
    ]
