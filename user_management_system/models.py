from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    class Meta:
        db_table = 'User_Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField