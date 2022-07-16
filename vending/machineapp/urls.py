from django.urls import path
from . import views

app_name = "machineapp"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('top/', views.top_view, name="top"),
    path('vending-machine/', views.vending_machine, name="vending-machine"),
    path('charge/', views.charge, name="charge"),
    path('purchase/', views.purchase, name="purchase"),
    path('change/', views.change, name="change"),
]
