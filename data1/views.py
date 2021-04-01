from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . models import Stock, Restock, Item, SellItem, DailyTotalSales
from django.urls import reverse_lazy
from . forms import AddItemForm, SellItemForm, NewItemForm, DailySalesForm
# Create your views here.
class DailySalesView(CreateView):
    model = DailyTotalSales
    form_class = DailySalesForm
    template_name = "data1/dailysales.html"

class DailyTotalSalesView(ListView):
    model = DailyTotalSales
    template_name = "data1/total_daily_sales.html"

class HomeListView(ListView):
    model = Stock
    template_name = "data1/home.html"


class StockDetailView(DetailView):
    model = Stock
    template_name = "data1/stock_detail.html"

class StockAddView(CreateView):
    model = Stock
    form_class = NewItemForm
    template_name = "data1/add_stock.html"

class ItemAddView(CreateView):
    model = Item
    form_class = AddItemForm
    template_name = "data1/restock.html"

class SellItemView(CreateView):
    model  = SellItem 
    form_class = SellItemForm
    template_name = "data1/sell.html"

class SalesView(ListView):
    model = SellItem
    template_name = "data1/sales.html"


class UpdatePriceView(UpdateView):
    model = Stock
    fields = ('buying_price', 'selling_price')
    template_name = "data1/update_price.html"
    success_url = reverse_lazy('home')
