from django.contrib import admin
from .models import UserProfile

# Register your models here.

# Display Experience field in admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience')  # Display these fields in the admin list view
    search_fields = ['user__username', 'experience']  # Allow searching by username and experience

# Register the model and the admin class
admin.site.register(UserProfile, UserProfileAdmin)