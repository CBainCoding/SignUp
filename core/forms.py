from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    experience_choices = (
        ('beginner', 'Beginner'),
        ('experienced', 'Experienced'),
    )
    experience = forms.ChoiceField(choices=experience_choices)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "form-control mb-3"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Your email",
        "class": "form-control mb-3"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control mb-3"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm password",
        "class": "form-control mb-3"
    }))
    experience = forms.ChoiceField(choices=experience_choices, widget=forms.Select(attrs={
        "class": "form-select mb-3"
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "experience")

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "form-control mb-3"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control mb-3"
    }))