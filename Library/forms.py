from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *



# create forms here
class SignupFormAdmin(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-pill fs-6', 'placeholder': 'Username'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg rounded-pill fs-6", 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg rounded-pill fs-6", 'placeholder': 'Password confirmation'}))
    is_admin = forms.BooleanField(label="I wanna join here as an admin",  required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_admin')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-pill fs-6', 'placeholder': 'Username'}),
        #     'is_admin': forms.CheckboxInput( attrs={"class": "form-check-input ms-3"}),
        #     'is_student': forms.CheckboxInput(attrs={"class": "form-check-input ms-2"}),
        # }

class SignupFormStudent(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-pill fs-6', 'placeholder': 'Username'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg rounded-pill fs-6", 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg rounded-pill fs-6", 'placeholder': 'Password confirmation'}))
    is_student = forms.BooleanField(label="I wanna join here as an student",  required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_student')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-pill fs-6', 'placeholder': 'Username'}),
        #     'is_admin': forms.CheckboxInput(attrs={"class": "form-check-input ms-3"}),
        #     'is_student': forms.CheckboxInput(attrs={"class": "form-check-input ms-2"}),
        # }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg mb-4 rounded-pill fs-6', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg mb-4 rounded-pill fs-6', 'placeholder': 'Password'}))

class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = "__all__"

class AdminProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = AdminProfile
        exclude = ('user',)