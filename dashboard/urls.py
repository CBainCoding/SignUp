from django.contrib.auth import views as auth_views
from django.urls import path
from .views import account_page, edit_user, delete_user


urlpatterns = [
    path('account/', account_page, name='account_page'),
    path('edit/', edit_user, name='edit_user'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),
    path('delete/', delete_user, name='delete_user'),
]
