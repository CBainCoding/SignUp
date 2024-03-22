from django.urls import path
from .views import submit_enquiry, enquiry_success

urlpatterns = [
    path('contact/', submit_enquiry, name='contact'),
    path('success/', enquiry_success, name='success'),
]