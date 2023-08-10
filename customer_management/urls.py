from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('services/', views.services, name="services"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('customers/', views.customer_list, name="customers"),
    path('contacts/', views.contact_list, name="contacts"),
    path('customer_create/', views.customer_create, name="customer_create"),
    path('customer/<int:id>/', views.customer_detail, name="customer_detail"),
    path('customer/<int:id>/gallery/add/', views.add_images_to_gallery, name="add_images"),
    path('customer_update/<int:id>/', views.customer_update, name="customer_update"),
    path('transaction_create/', views.transaction_create, name="transaction_create"),
    path('transaction_update/<int:id>/', views.transaction_update, name="transaction_update"),
    path('transaction_detail/<int:id>/', views.transaction_detail, name="transaction_detail"),

    path('transactions/', views.transactions, name="transactions"),
    path('projects/', views.projects, name="projects"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('customer_search/', views.customer_search, name="customer_search"),
    path('image_search/', views.image_search, name="image_search"),
    path('transaction_search/', views.transaction_search, name="transaction_search"),


    path('api/monthly-sales/', views.monthly_sales_data, name='monthly_sales_data'),
    path('api/weekly-sales/', views.weekly_sales_data, name='weekly_sales_data'),
    path('api/weekly-views/', views.weekly_views_data, name='weekly_views_data'),
    path('add-images/', views.add_images_to_gallery, name='add_images'),
]
