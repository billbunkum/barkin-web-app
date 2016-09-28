from django.contrib.auth.models import User

from django.db import models

class UserProfile(models.Model):

    user = models.ForeignKey(User)
#   table has user_id now

    bio = models.CharField(max_length=200)
    url = models.URLField("Website", blank=True)
#   img_gravatar = ...