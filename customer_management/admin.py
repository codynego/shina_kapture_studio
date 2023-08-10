from django.contrib import admin
from .models import Customer, Gallery, ServiceTransaction, Analytics, Contact, Image

# Register your models here.
admin.site.register(Customer)
admin.site.register(ServiceTransaction)
admin.site.register(Analytics)
admin.site.register(Contact)
admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model = Gallery.images.through
    extra = 1  # Number of empty forms to display

@admin.register(Gallery)
class GalleriAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

