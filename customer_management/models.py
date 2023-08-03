from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    

class Gallery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.customer.name
    

class ServiceTransaction(models.Model):
    SERVICE_TYPE = (
        ("passport", "passport"),
        ("photoshoot", "photoshoot"),
        ("photo_printing", "photo_printing")
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=20)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=20)
    balance = models.DecimalField(decimal_places=2, max_digits=20)
    images = models.ForeignKey(Gallery, on_delete=models.CASCADE)


    def __str__(self):
        return self.customer.name
     