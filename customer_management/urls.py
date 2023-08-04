from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('customers/', views.customer_list, name="customers"),
    path('customer_create/', views.customer_create, name="customer_create"),
    path('transaction_create/', views.transaction_create, name="transaction_create"),

    path('transactions/', views.transactions, name="transactions"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]