from django.db import models
from django.conf import settings

# Create your models here.

class Enquiry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"Enquiry by {self.user.username}"