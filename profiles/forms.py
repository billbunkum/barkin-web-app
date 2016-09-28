from django import forms
from django.shortcuts import render, redirect

from .models import UserProfile

#url, bio, user_id
class ProfileForm(forms.ModelForm):
    pass