# faq/urls.py
from django.urls import path
from .views import faqs_page

urlpatterns = [
    path('faqs/', faqs_page, name='faqs_page'),
]
