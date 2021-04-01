from django.contrib import admin

from . models import Item, Stock, SellItem, Restock, UpdatePrice, DailyTotalSales
# Register your models here.
@admin.register(DailyTotalSales)
class DailyTotalSalesAdmin(admin.ModelAdmin):
    list_display = ("sales_number", "item_code", "amount", "sales_date")



@admin.register(Restock)
class RestockAdmin(admin.ModelAdmin):
    list_display = ("restock_number", "item_name", "item_code", "quantity")
    prepopulated_fields = {'item_code': ('item_name',),}



@admin.register(SellItem)
class SellItemAdmin(admin.ModelAdmin):
    list_display = ("selling_number","stock" ,"item_code", "sold_quantity", "sales_amount", "date_sold")
    

@admin.register(UpdatePrice)
class UpdatePriceAdmin(admin.ModelAdmin):
    list_display = ("item_name","item_code", "buying_price", "selling_price")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("stock_item_code", "item_code", "quantity", "date_recorded")
    prepopulated_fields = {'item_code': ('stock_item_code',)}


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "item_code", "item_name", "buying_price",
                    "selling_price", "available_items")
