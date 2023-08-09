from django.contrib import admin
from .models import Customer, Gallery, ServiceTransaction, Analytics, Contact

# Register your models here.
admin.site.register(Customer)
admin.site.register(Gallery)
admin.site.register(ServiceTransaction)
admin.site.register(Analytics)
admin.site.register(Contact)