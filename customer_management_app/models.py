from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
    

class Gallary(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.customer.user.username
    

class Service_transaction(models.Model):
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
    images = models.ForeignKey(Gallary, on_delete=models.CASCADE)


    def __str__(self):
        return self.customer.user.username
     