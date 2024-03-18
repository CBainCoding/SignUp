from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserEditForm, UserProfileEditForm

# Create your views here.

@login_required
def account_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'user_profile': user_profile,
    }
    return render(request, 'account_page.html', context)

@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance=request.user.userprofile, data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('dashboard:account_page')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)
    
    return render(request, 'edit_account.html', {'user_form': user_form, 'profile_form': profile_form})