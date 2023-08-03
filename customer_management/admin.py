from django.contrib import admin
from .models import Customer, Gallery, ServiceTransaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Gallery)
admin.site.register(ServiceTransaction)