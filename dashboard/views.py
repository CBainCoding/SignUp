from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserEditForm, UserProfileEditForm
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

# Account Page view
@login_required
def account_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'user_profile': user_profile,
    }
    return render(request, 'account_page.html', context)

# Edit account info form
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

# Delete account view
@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.warning(request, 'Your account has been deleted successfully.')
        return redirect('/')
    else:
        return render(request, 'confirm_delete.html')