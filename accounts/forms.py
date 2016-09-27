from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#from django.conf import settings
from django import forms

#will eventually need BootstrapFormMixin
class LoginForm(AuthenticationForm):
    pass

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Passphrase', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Passphrase', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passphrases are different!')

        return cd['password2']