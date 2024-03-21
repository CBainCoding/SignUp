from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import FAQ
from .forms import FAQForm

# Create your views here.

#Code to render FAQ instances on FAQ page
def faqs_page(request):
     # Retrieve all FAQs from the database
    faqs = FAQ.objects.all()

    # Pass the FAQs to the template
    return render(request, 'faqs.html', {'faqs': faqs})

# Mixin to only allow staff-level users access
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class FAQCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faqs/faq_form.html'
    success_url = reverse_lazy('faqs:faqs_page')

    def form_valid(self, form):
        response = super(FAQCreateView, self).form_valid(form)
        messages.success(self.request, 'FAQ created successfully.')
        return response

class FAQUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faqs/faq_form.html'
    success_url = reverse_lazy('faqs:faqs_page')

    def form_valid(self, form):
        response = super(FAQUpdateView, self).form_valid(form)
        messages.success(self.request, 'FAQ updated successfully.')
        return response

class FAQDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = FAQ
    template_name = 'faqs/faq_confirm_delete.html'
    success_url = reverse_lazy('faqs:faqs_page')

    def delete(self, request, *args, **kwargs):
        response = super(FAQDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'FAQ deleted successfully.')
        return response