from django.db import models

from profiles.models import UserProfile

class Bark(models.Model):

    profile = models.ForeignKey(UserProfile)
    content = models.CharField(max_length=120)
    post_date = models.DateTimeField(auto_now_add=True)