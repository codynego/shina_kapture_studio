from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
    

class Service_transaction(models.Model):
    SERVICE_TYPE = {
        "passport": "passport",
        "photoshoot": "photoshoot",
        "photo_printing": "photo_printing"
    }
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
