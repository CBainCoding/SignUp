from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from dashboard.models import UserProfile

class SignupForm(UserCreationForm):
    # Custom fields for experience
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    experience_choices = (
        ('beginner', 'Beginner - Little to no experience with archery'),
    ('experienced', 'Experienced - Has completed a basic competency certificate.'),
)
    experience = forms.ChoiceField(choices=experience_choices, widget=forms.RadioSelect(attrs={
        "class": "form-check-input"
    }))

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
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "experience")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.experience = self.cleaned_data['experience']
            user_profile.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "form-control mb-3"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control mb-3"
    }))