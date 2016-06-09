from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserExtra(models.Model):
	# Links UserExtra to User model instance.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	#Extra attributes added to user
	phoneNumber = models.CharField(max_length=30, blank=True)
