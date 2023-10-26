from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import LabUser

# from django.forms import ModelForm
# from .models import CustomUser
# from django.db import models

# from django.forms.widgets import FileInput



class UserAdminCreationForm(UserCreationForm):

    """
    A Custom form for creating new users.
    """
    style = "border-radius: 8px; border: 1px lightgrey solid"
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-box', 
        'placeholder': 'First Name',
        'style': style
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-box', 'placeholder': 'Last Name', 'style': style}))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control text-box', 'placeholder': 'Mobile', 'style': style}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control text-box', 'placeholder': 'Email', 'style': style}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-box', 'placeholder': 'Password', 'style': style}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-box', 'placeholder': 'Confirm Password', 'style': style}))

    class Meta:    
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2']






class LabRegistrationForm(forms.ModelForm):
    lab_email = forms.EmailField(label='Email')
    lab_password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = LabUser
        fields = ['lab_name', 'lab_owner', 'lab_email', 'lab_password', 'details']
        labels = {
            'lab_email': 'Email',
            'lab_password': 'Password',
        }



class LabLoginForm(forms.Form):
    lab_email = forms.EmailField()
    lab_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        lab_email = cleaned_data.get('lab_email')
        lab_password = cleaned_data.get('lab_password')

        if lab_email and lab_password:
            # You can add additional validation logic here if needed
            pass

        return cleaned_data