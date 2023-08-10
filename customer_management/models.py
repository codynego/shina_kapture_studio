from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
import random



class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=25, null=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.name
    

class Image(models.Model):

    WIDTH = (
        ("large-small-height", "large-small-height"),
        ("small-height", "small-height"),
        ("medium-large-height", "medium-large-height"),
        ("medium-small-height", "medium-small-height"),
        ("large-height", "large-height"),

    )

    AGE_GROUP = (
        ("below 1 year", "below 1 year"),
        ("teenager", "teenager"),
        ("adult", "adult")
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    age = models.CharField(max_length=20, choices=AGE_GROUP, null=True)
    image = models.ImageField(upload_to='images/')
    image_width = models.CharField(max_length=20, choices=WIDTH, editable=False, null=True)
    status = models.BooleanField(default=False, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.id}"
    
    def save(self, *args, **kwargs):
        if not self.image_width:
            self.image_width = random.choice([choice[0] for choice in self.WIDTH])
        super().save(*args, **kwargs)                      

    

class Gallery(models.Model):
    CATEGORY = (
        ("fashion", "wedding"),
        ("lifestyle", "birthday"),
        ("natural", "family pics"),
        ("videos", "others")
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True, choices=CATEGORY)
    date = models.DateField(auto_now_add=True, null=True)

    images = models.ManyToManyField(Image)

    def __str__(self):
        return f"{self.title}-{self.customer.name}-{self.id}"
    
    

class ServiceTransaction(models.Model):
    SERVICE_TYPE = (
        ("passport", "passport"),
        ("Hardcopy", "Hardcopy"),
        ("Softcopy", "Softcopy"),
        ("photo_printing", "photo_printing"),
        ("others", "others")
    )

    PAYMENT_TYPE = (
        ("Transfer", "Transfer"),
        ("Cash", "Cash"),
        ("POS", "POS")
    )

    STATUS = (
        ("completed", "completed"),
        ("in progress", "in progress"),
        ("cancelled", "cancelled")
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=SERVICE_TYPE)
    quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=20)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=20)
    balance = models.DecimalField(decimal_places=2, max_digits=20)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_TYPE, null=True)
    images = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    job_status = models.CharField(max_length=20, choices=STATUS, null=True)


    def __str__(self):
        return "f{self.customer.name}-{self.id}"
    

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')


class Analytics(models.Model):
    views = models.PositiveIntegerField(null=True, default=0)
    date = models.DateField(auto_now_add=True, null=True)


     