from django.urls import path
from .views import faqs_page, FAQCreateView, FAQUpdateView, FAQDeleteView


urlpatterns = [
    path('', faqs_page, name='faqs_page'),
    path('create/', FAQCreateView.as_view(), name='faq_create'),
    path('edit/<int:pk>/', FAQUpdateView.as_view(), name='faq_edit'),
    path('delete/<int:pk>/', FAQDeleteView.as_view(), name='faq_delete'),
]
