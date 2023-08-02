from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import UserForm

# Create your views here.


def index(request):
    return render(request, 'dashboard/main.html')


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard/customerlist.html', {'customers': customers})

