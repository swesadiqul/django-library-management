from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create forms
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


    
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'username':forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email':forms.TextInput(attrs={'class': 'form-control mb-3'}),
            # 'password':forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2':forms.PasswordInput(attrs={'class': 'form-control'}),
        }