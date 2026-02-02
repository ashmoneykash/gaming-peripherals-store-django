from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product),
    path('orders/', views.view_orders),
    path('sales/', views.sales_report),
]
