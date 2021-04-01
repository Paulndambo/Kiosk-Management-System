from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import datetime, date

# Create your models here.


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=200, unique=True)
    item_name = models.CharField(max_length=200)
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    available_items = models.IntegerField(default=0)

    def __str__(self):
        return self.item_code
    
    def get_absolute_url(self):
        return reverse_lazy("home")

class Restock(models.Model):
    restock_number = models.AutoField(unique=True, primary_key=True)
    item_name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.item_name)

    def get_absolute_url(self):
        return reverse_lazy("home")
    

class Item(models.Model):
    stock_item_code = models.ForeignKey(Stock, on_delete=models.CASCADE)
    item_code = models.CharField(
        max_length=200, null=True, help_text="Similar to stock_item_code above")
    quantity = models.IntegerField()
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.stock_item_code)

    def get_absolute_url(self):
        return reverse_lazy("home")


class UpdatePrice(models.Model):
    item_name = models.OneToOneField(Stock, on_delete=models.CASCADE, null=True)
    item_code = models.CharField(max_length=200)
    buying_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.item_code)

    def get_absolute_url(self):
        return reverse_lazy("home")


class SellItem(models.Model):
    sell_number = models.AutoField(unique=True, primary_key=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=200, null=True)
    sold_quantity = models.IntegerField(default=0)
    selling_price = models.FloatField(default=0)
    date_sold = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.sell_number)

    def get_absolute_url(self):
        return reverse_lazy("home")

    def selling_number(self):
        return "SN/"+str(self.sell_number)

    def sales_amount(self):
        return self.selling_price * self.sold_quantity

    class Meta:
        verbose_name_plural = ("Sold Items")
 
class DailyTotalSales(models.Model):
    sales_number = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    sales_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_code

    def get_absolute_url(self):
        return reverse_lazy("home")

    class Meta:
        verbose_name_plural = ("Daily Total Sales")

class TotalSales(models.Model):
    sales_number = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=200)
    total_sales = models.FloatField(default=0)

    def __str__(self):
        return self.item_code
    

    
    
