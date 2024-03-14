# faq/urls.py
from django.urls import path
from .views import faqs_page


app_name = 'faqs'

urlpatterns = [
    path('', faqs_page, name='faqs_page'),
]