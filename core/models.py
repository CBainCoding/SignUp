from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Core(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=20, choices=(
        ('beginner', 'Beginner'),
        ('experienced', 'Experienced'),
    ))

    def __str__(self):
        return self.user.username