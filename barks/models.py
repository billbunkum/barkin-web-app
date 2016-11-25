from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

#from profiles.models import UserProfile

class Bark(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
#    profile = models.ForeignKey(UserProfile)
    content = models.CharField(max_length=60)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("barks:edit_bark", args=[self.pk])
