from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile

# Create your views here.

@login_required
def account_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'user_profile': user_profile,
    }
    return render(request, 'account_page.html', context)