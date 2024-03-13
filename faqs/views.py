from django.shortcuts import render
from .models import FAQ

# Create your views here.

#Code to render FAQ instances on FAQ page
def faqs_page(request):
     # Retrieve all FAQs from the database
    faqs = FAQ.objects.all()

    # Pass the FAQs to the template
    return render(request, 'faqs.html', {'faqs': faqs})