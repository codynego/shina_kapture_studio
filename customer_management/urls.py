from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('customers/', views.customer_list, name="customers"),
    path('customer_create/', views.customer_create, name="customer_create")
]