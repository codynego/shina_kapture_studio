from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

# Create your views here.


def index(request):
    return render(request, 'dashboard/customers.html')


def customer_list(request):
    customers = Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'dashboard/customers.html', context)


def customer_create(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to a customer list page or any other page
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {'form': form})

