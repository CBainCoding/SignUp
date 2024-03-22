from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm


urlpatterns = [
    path('', views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html",
                                                authentication_form=LoginForm), name="login"),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
]
