from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.


def index(request):
    return render(request, 'home.html')


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customerlist.html', {'customers': customers})

"""def customer_create(request):
    if request.method == "POST":
        content = request.get.POST
    #if content."""
