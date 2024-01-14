from django.db import models
from django.contrib.auth.models import User


# Model for User Information
class UserInformation(models.Model):
    # Link to Django's built-in User model for authentication
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields like subscription status can be added here
    subscription_status = models.CharField(max_length=100)
    access_level = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username