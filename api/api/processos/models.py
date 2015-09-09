from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Process(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user')
	number = models.CharField(max_length=20, validators=[RegexValidator("^[0-9]*$")])
	data = models.TextField()
