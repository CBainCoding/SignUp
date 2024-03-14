from django.shortcuts import render

from .forms import SignupForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def signup (request):
    form = SignupForm()

    return render(request, "core/signup.html", {
        "form": form
    })