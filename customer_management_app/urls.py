from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('cust/', views.customer_list, name="cust")
]