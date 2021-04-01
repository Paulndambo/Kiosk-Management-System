from django import forms
from . models import Stock, Item, Restock, UpdatePrice, SellItem, DailyTotalSales

choices = Stock.objects.all().values_list('item_code', 'item_code')
choice_list = []

for item in choices:
    choice_list.append(item)

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('stock_item_code', 'item_code', 'quantity')

        widgets = {
            'stock_item_code': forms.Select(attrs={'class': 'form-control'}),
            'item_code': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),          
        }

class DailySalesForm(forms.ModelForm):
    class Meta:
        model = DailyTotalSales
        fields = ('item_code',)

        widgets = {
            'item_code': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }



class SellItemForm(forms.ModelForm):
    class Meta:
        model = SellItem
        fields = ('stock', 'item_code', 'sold_quantity')

        widgets = {
            'stock': forms.Select(attrs={'class': 'form-control'}),
            'item_code': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'sold_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('item_code', 'item_name', 'buying_price',
                  'selling_price', 'available_items')

        widgets = {
            'item_code': forms.TextInput(attrs={'class': 'form-control'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'buying_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available_items': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
