from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer, ServiceTransaction, Gallery, Analytics, Contact, Image
from .forms import CustomerForm, LoginForm, TransactionForm, TransactionCreateForm, GalleryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime, timedelta
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
import json
from django.urls import reverse




def home(request):
    today = datetime.now().date()
    instance, created = Analytics.objects.get_or_create(date=today)
    instance.views += 1
    instance.save()

    items_per_page = 5
    gallery = Image.objects.filter(status=True)
    paginator = Paginator(gallery, items_per_page)

    page_number = request.GET.get('page')  # Get the requested page number from the URL parameter
    page = paginator.get_page(page_number)

    context = {
        "gallerys": page,
        "page": page
    }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(name)

        submission = Contact(name=name, email_address=email, phone_number=phone, message=message)
        submission.save()

        return redirect('home')
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, "about.html")

def portfolio(request):
    items_per_page = 5
    gallery = Gallery.objects.filter(status=True)
    paginator = Paginator(gallery, items_per_page)

    page_number = request.GET.get('page')  # Get the requested page number from the URL parameter
    page = paginator.get_page(page_number)

    context = {
        "gallerys": page,
        "page": page
    }
    return render(request, "portfolio.html", context)


def services(request):
    return render(request, "services.html")


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
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    total_amount_today = ServiceTransaction.objects.filter(date=today).aggregate(total_amount_today=Sum('amount_paid'))['total_amount_today'] or 0
    total_amount_yesterday = ServiceTransaction.objects.filter(date=yesterday).aggregate(total_amount_yesterday=Sum('amount_paid'))['total_amount_yesterday'] or 0
    total_money = ServiceTransaction.objects.aggregate(total_money=Sum('amount_paid'))['total_money'] or 0
    total_customers = Customer.objects.count()
    new_customer = Customer.objects.filter(date=today).count()
    today_customers = ServiceTransaction.objects.filter(date=today).count() or 0
    yesterday_customers = ServiceTransaction.objects.filter(date=yesterday).count() or 0

    if total_amount_yesterday != 0:
        percentage_change = ((total_amount_today - total_amount_yesterday) / total_amount_yesterday) * 100
        sales_percent = round((percentage_change / total_amount_yesterday) * 100, 2)
    else:
        sales_percent = 0

    if yesterday_customers != 0:
        yesterday_percentage_change = ((today_customers - yesterday_customers) / yesterday_customers) * 100
        ycust_percent = round((yesterday_percentage_change / yesterday_customers) * 100, 2)
    else:
        ycust_percent = 0

    today = timezone.now()
    last_month_start = today.replace(day=1, month=today.month-1)
    last_month_end = last_month_start + timedelta(days=30)

    this_month_start = today.replace(day=1, month=today.month)
    this_month_end = last_month_start + timedelta(days=30)

    last_month_sales = ServiceTransaction.objects.filter(date__range=(last_month_start, last_month_end)).aggregate(total_amount_paid_last_month=Sum('amount_paid'))['total_amount_paid_last_month'] or 0
    this_month_sales = ServiceTransaction.objects.filter(date__range=(this_month_start, this_month_end)).aggregate(total_amount_paid_last_month=Sum('amount_paid'))['total_amount_paid_last_month'] or 0

    last_month_customer = Customer.objects.filter(date__range=(last_month_start, last_month_end)).count() or 0
    this_month_customer = Customer.objects.filter(date__range=(this_month_start, this_month_end)).count() or 0


    this_month_projects = ServiceTransaction.objects.filter(date__range=(this_month_start, this_month_end)).count() or 0

    if last_month_sales != 0:
        monthly_percentage_sales = ((this_month_sales - last_month_sales) / last_month_sales) * 100
        monthly_sales = round((monthly_percentage_sales / last_month_sales) * 100, 2)
    else:
        monthly_sales = 0

    if last_month_customer != 0:
        monthly_percentage_customer = ((this_month_customer - last_month_customer) / last_month_customer) * 100
        monthly_customer = round((monthly_percentage_customer / last_month_customer) * 100, 2)
    else:
        monthly_customer = 0


    trans_per_page = 10
    projects = ServiceTransaction.objects.exclude(
                Q(type="passport") |
                Q(type="others") |
                Q(job_status="in progress") |
                Q(job_status="cancelled")
            )
    trans_paginator = Paginator(projects, trans_per_page)

    page_number = request.GET.get('page')
    page = trans_paginator.get_page(page_number)


    context = {
        'total_money': total_money,
        'total_customers': total_customers,
        'total_amount_today': total_amount_today,
        'total_amount_yesterday': total_amount_yesterday,
        'new_customer': new_customer,
        'today_customers': today_customers,
        'sales_percent': sales_percent,
        'monthly_sales': monthly_sales,
        'ycust_percent': ycust_percent,
        'monthly_customer': monthly_customer,
        "projects": page,
        "this_month_projects": this_month_projects
    }

    return render(request, 'dashboard/main.html', context)



@login_required
def customer_list(request):
    items_per_page = 20
    customers = Customer.objects.all()
    paginator = Paginator(customers, items_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "customers": page,
        "page": page
    }
    return render(request, 'dashboard/customers.html', context)



@login_required
def contact_list(request):
    items_per_page = 20
    contact = Contact.objects.all()
    paginator = Paginator(contact, items_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "contacts": page,
        "page": page
    }
    return render(request, 'dashboard/contacts.html', context)


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
def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', id=customer.id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'dashboard/customer_update.html', {'form': form, "customer": customer})


@login_required
def transactions(request):
    items_per_page = 20
    transactions = ServiceTransaction.objects.all()
    paginator = Paginator(transactions, items_per_page)

    page_number = request.GET.get('page')  # Get the requested page number from the URL parameter
    page = paginator.get_page(page_number)

    context = {
        "transactions": page,
        "page": page
    }

    return render(request, 'dashboard/transactions.html', context)


@login_required
def projects(request):
    trans_per_page = 5
    projects = ServiceTransaction.objects.exclude(
                Q(type="passport") |
                Q(type="others")
            )
    trans_paginator = Paginator(projects, trans_per_page)

    page_number = request.GET.get('page')
    page = trans_paginator.get_page(page_number)

    context = {
        "projects": page,
        "page": page
    }

    return render(request, 'dashboard/projects.html', context)



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


@login_required
def transaction_update(request, id):
    transaction = get_object_or_404(ServiceTransaction, id=id)
    if request.method == "POST":
        form = TransactionCreateForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_detail', id=transaction.id)
            
    else:
        form = TransactionCreateForm(instance=transaction)

    return render(request, 'dashboard/transaction_update.html', {'form': form, "transaction": transaction})


@login_required
def transaction_detail(request, id):
    if request.user.is_authenticated:
        if ServiceTransaction.objects.filter(id=id).exists:
            transaction = ServiceTransaction.objects.get(id=id)
            customer = Customer.objects.get(id=transaction.customer.id)
            gallery = Image.objects.filter(customer=customer)
            
            items_per_page = 10
            paginator = Paginator(gallery, items_per_page)
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)

            context = {
                "transaction": transaction,
                "gallery": gallery,
                'page': page
            }
        else:
            return HttpResponse("404 not found")
        return render(request, 'dashboard/transaction_detail.html', context)
    else:
        return redirect('login')


@login_required
def customer_detail(request, id):
    if request.user.is_authenticated:
        if Customer.objects.filter(id=id).exists:
            customer = Customer.objects.get(id=id)
            gallery = Image.objects.filter(customer=customer)

            items_per_page = 10
            paginator = Paginator(gallery, items_per_page)
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)

            context = {
                "customer": customer,
                "gallery": gallery,
                'page': page
            }
        else:
            return HttpResponse("404 not found")
        return render(request, 'dashboard/customer_detail.html', context)
    else:
        return redirect('login')
    

@login_required
def gallery(request):
    items_per_page = 15
    query = request.GET.get('q')  # Get the search query from the URL parameter

    if query:
        gallerys = Image.objects.filter(
            Q(name__icontains=query) | 
            Q(age__icontains=query) |
            Q(date__icontains=query) 
        )
    else:
        gallerys = Image.objects.all()

    paginator = Paginator(gallerys, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "gallerys": page, 
        "page": page,
    }
    return render(request, 'dashboard/gallery.html', context)

def add_images_to_gallery(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        #description = request.POST['description']
        age_group = request.POST['age']
        category  = request.POST['category']
        images = request.FILES.getlist('images')

        # Create a new gallery entry
        customer = Customer.objects.get(id=id)
        gallery = Gallery.objects.create(title=title, customer=customer, category=category)


        # Save the images to the gallery
        for image in images:
            gallery.images.create(customer=customer, image=image, age=age_group)

        return redirect(reverse('customer_detail', args=[id]))  # Redirect to the gallery page

    return render(request, 'dashboard/add_images.html')

from django.http import JsonResponse


def customer_search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query != '':
            customers = Customer.objects.filter(
                Q(name__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(id__icontains=query)
            )
        else:
            customers = customers.objects.all()
        data = {
            "customers": [
                {
                    "id": customer.id,
                    "name": customer.name,
                    "phone_number": customer.phone_number,
                    "address": customer.address,
                    "date": customer.date,
                } for customer in customers
            ]
        }
        return JsonResponse(data)
    

def image_search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query != '':
            gallerys = Gallery.objects.filter(
                Q(customer__name__icontains=query) |
                Q(category__icontains=query) |
                Q(age__icontains=query)
            )
        else:
            gallerys = Gallery.objects.all()
        data = {
            "gallerys": [
                {
                    "id": gallery.id,
                    "name": gallery.customer.name,
                    "category": gallery.category,
                    "date": gallery.date,
                    "width": gallery.image_width,
                    "url": gallery.images.url
                } for gallery in gallerys
            ]
        }
        return JsonResponse(data)
    

def transaction_search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query != '':
            transactions = ServiceTransaction.objects.filter(
            Q(customer__name__icontains=query) |
            Q(type__icontains=query) |
            Q(id__icontains=query)
            )
        else:
            transactions = ServiceTransaction.objects.all()

        data = {
            "transactions": [
                {
                    "id": transaction.id,
                    "name": transaction.customer.name,
                    "type": transaction.type,
                    "quantity": transaction.quantity,
                    "total_amount": transaction.total_amount,
                    "amount_paid": transaction.amount_paid,
                    "payment_method": transaction.payment_method,
                    "balance": transaction.balance,
                    "created_at": transaction.date,
                } for transaction in transactions
            ]
        }
        return JsonResponse(data)

def search_form_view(request):
    customers = Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, 'dashboard/search.html', context)


def monthly_sales_data(request):
    today = datetime.now().date()

    # Create a list to store the sum of sales for each month
    monthly_sales = []

    for i in range(12):
        month = today.replace(month=today.month-i, day=1)
        next_month = month.replace(month=month.month+1) if month.month < 12 else month.replace(year=month.year+1, month=1)
        
        total_amount = ServiceTransaction.objects.filter(date__range=(month, next_month - timedelta(days=1))).aggregate(total_amount=Sum('amount_paid'))['total_amount'] or 0
        monthly_sales.insert(0, total_amount)

    return JsonResponse({'monthly_sales': monthly_sales})


def weekly_sales_data(request):
    today = datetime.now().date()

    weekly_sales = [0] * 7

    for i in range(7):
        day = today - timedelta(days=i)
        day_of_week = day.weekday()

        total_amount = ServiceTransaction.objects.filter(date=day).aggregate(total_amount=Sum('amount_paid'))['total_amount'] or 0
        weekly_sales[day_of_week] = total_amount

    return JsonResponse({'weekly_sales': weekly_sales})



def weekly_views_data(request):
    today = datetime.now().date()

    # Create a list to store the sum of views for each day of the week
    weekly_views = [0] * 7  # Initialize with zeros for each day

    for i in range(7):
        day = today - timedelta(days=i)
        day_of_week = day.weekday()  # Get the day of the week (0 = Monday, 6 = Sunday)

        total_views = Analytics.objects.filter(date=day).aggregate(total_views=Sum('views'))['total_views'] or 0  # Count the number of views
        weekly_views[day_of_week] = total_views  # Update the views count in the correct day slot

    return JsonResponse({'weekly_views': weekly_views})