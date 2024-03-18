from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

#This edits the standard "user" and should pull through to "user profile"
class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# This edits the custom extended user profile
class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('experience',)