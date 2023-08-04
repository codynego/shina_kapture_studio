from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, ServiceTransaction, Gallery
from .forms import CustomerForm, LoginForm, TransactionForm, TransactionCreateForm, GalleryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    
    context = {
        "form": form
    }
    return render(request, "dashboard/login.html", context)
    

def user_logout(request):
    logout(request)
    return redirect('login')  
  

@login_required
def dashboard(request):
    return render(request, 'dashboard/main.html')

@login_required
def customer_list(request):
    customers = Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'dashboard/customers.html', context)

@login_required
def customer_create(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')  # Redirect to a customer list page or any other page
    else:
        form = CustomerForm()
    return render(request, 'dashboard/customer_create.html', {'form': form})

@login_required
def transactions(request):
    transactions = ServiceTransaction.objects.all()

    context = {
        "transactions": transactions
    }
    return render(request, 'dashboard/transactions.html', context)



@login_required
def transaction_create(request):
    form = TransactionCreateForm()
    if request.method == "POST":
        form = TransactionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions')  # Redirect to a customer list page or any other page
    else:
        form = TransactionCreateForm()
    return render(request, 'dashboard/transaction_create.html', {'form': form})

def gallery(request):
    gallerys = Gallery.objects.all()
    context = {
        'gallerys': gallerys
    }
    return render(request, 'dashboard/gallery.html', context)

"""def add_gallery_item(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryForm()
    return render(request, 'gallery/add_gallery_item.html', {'form': form})"""