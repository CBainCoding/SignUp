from django import forms
from .models import FAQ



# Form to allow front-end addition of FAQs. 
# This will allow staff-level users access without needing to access the admin panel

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']