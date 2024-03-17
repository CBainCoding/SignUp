from django.contrib import admin
from .models import UserProfile

# Register your models here.

# Display Experience field in admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'experience')  # Ensuring experience is included

    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'experience']  # Allow searching by these fields

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    def experience(self, obj):
        return obj.experience  # Direct attribute of UserProfile, no method needed, but listed for consistency

    # Setting short descriptions for custom methods
    username.short_description = 'Username'
    first_name.short_description = 'First Name'
    last_name.short_description = 'Last Name'
    email.short_description = 'Email'
    experience.short_description = 'Experience'  # Ensuring this is clear

# Register the model and the admin class
admin.site.register(UserProfile, UserProfileAdmin)