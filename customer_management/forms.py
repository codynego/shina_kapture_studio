from django import forms
from .models import Customer, User, ServiceTransaction, Gallery, UploadedImage


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ["id","name", "phone_number", "email_address", "address"]


    def __init__(self, *args, **kwargs):
        # Get the instance from the kwargs (if available)
        instance = kwargs.get('instance', None)
        # Call the parent __init__ method
        super(CustomerForm, self).__init__(*args, **kwargs)
        
        # Set default values from the instance if available
        if instance:
            self.fields['name'].initial = instance.name
            self.fields['phone_number'].initial = instance.phone_number
            self.fields['email_address'].initial = instance.email_address
            self.fields['address'].initial = instance.address

class TransactionForm(forms.ModelForm):
    
    class Meta:
        model = ServiceTransaction
        fields = "__all__"



class TransactionCreateForm(forms.ModelForm):

    class Meta:
        model = ServiceTransaction
        fields = ["customer", "type", "quantity", "total_amount", "amount_paid", "balance", "payment_method", "job_status"]

    
    def __init__(self, *args, **kwargs):
        # Get the instance from the kwargs (if available)
        instance = kwargs.get('instance', None)
        # Call the parent __init__ method
        super(TransactionCreateForm, self).__init__(*args, **kwargs)

        # Set default values from the instance if available
        if instance:
            self.fields['type'].initial = instance.type
            self.fields['quantity'].initial = instance.quantity
            self.fields['total_amount'].initial = instance.total_amount
            self.fields['amount_paid'].initial = instance.amount_paid
            self.fields['balance'].initial = instance.balance
            self.fields['payment_method'].initial = instance.payment_method
            self.fields['job_status'].initial = instance.job_status

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery 
        fields = ['customer', 'title', 'description', 'images', 'category']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()

