from django import forms

from .models import Bark

class BarkForm(forms.ModelForm):

    class Meta:
        model = Bark
        fields = ('content',)