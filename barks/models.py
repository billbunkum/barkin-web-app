from django.db import models
from django.contrib.auth.models import User

#from profiles.models import UserProfile

class Bark(models.Model):
    user = models.ForeignKey(User)
#    profile = models.ForeignKey(UserProfile)
    content = models.CharField(max_length=120)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.name = name