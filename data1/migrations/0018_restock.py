# Generated by Django 3.1.5 on 2021-03-31 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data1', '0017_auto_20210331_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restock',
            fields=[
                ('restock_number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data1.stock')),
            ],
        ),
    ]
