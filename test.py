import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yjstock.settings')
django.setup()

from django.contrib.auth.models import User
from user_management_system.models import UserProfile

# Now you can use Django ORM
print(UserProfile.objects.all())
