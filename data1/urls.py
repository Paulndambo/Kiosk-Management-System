from django.urls import path
from . views import HomeListView, ItemAddView, DailySalesView, DailyTotalSalesView, SellItemView, StockDetailView, UpdatePriceView, StockAddView, SalesView

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("restock/", ItemAddView.as_view(), name="restock"),
    path("sell/", SellItemView.as_view(), name="sell"),
    path("stock/<int:pk>/", StockDetailView.as_view(), name="stock_details"),
    path("stock/update_stock/<int:pk>/", UpdatePriceView.as_view(), name="update_stock"),
    path("add_stock/", StockAddView.as_view(), name="add_stock"),
    path("sales/", SalesView.as_view(), name="sales"),
    path("add_daily_stock/", DailySalesView.as_view(), name="add_daily_stock"),
    path("total_daily_sales/", DailyTotalSalesView.as_view(), name="total_daily_sales"),
]
