from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=20, choices=(
        ('beginner', 'Beginner'),
        ('experienced', 'Experienced'),
    ))

    def __str__(self):
        return self.user.username