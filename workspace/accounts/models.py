from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(primary_key=True)
    last_login = models.DateTimeField(default=timezone.now)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'
    is_authenticated = True
    is_anonymous = False
