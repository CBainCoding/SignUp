from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    experience_choices = (
        ('beginner', 'Beginner'),
        ('experienced', 'Experienced'),
    )
    experience = forms.ChoiceField(choices=experience_choices)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "experience")