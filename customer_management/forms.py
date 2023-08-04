from django import forms
from .models import Customer, User, ServiceTransaction, Gallery


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ["id","name", "phone_number", "email_address", "address"]

class TransactionForm(forms.ModelForm):
    
    class Meta:
        model = ServiceTransaction
        fields = "__all__"



class TransactionCreateForm(forms.ModelForm):

    class Meta:
        model = ServiceTransaction
        fields = ["customer", "type", "quantity", "total_amount", "amount_paid", "balance"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery 
        fields = ['customer', 'title', 'description', 'images', 'category']
