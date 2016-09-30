from django import forms
from django.contrib.auth.models import User

from .models import Bark

class BarkForm(forms.ModelForm):

    class Meta:
        model = Bark
        fields = ('content',)