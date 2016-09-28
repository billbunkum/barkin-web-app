from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from .models import UserProfile

def profile_list(request):
    profile_set = UserProfile.objects.all()
    usernames = profile_set.user_id

    context = {
        "profile_set": profile_set,
        "usernames": usernames,
    }

    return render(request, "profiles/profile_list.html", context)

def user_profile(request):
    user_profile = ProfileForm.objects.all()

    return render(request, "profiles/user_profile.html")

@login_required
def add_profile_info(request):
    if request.method == "POST":
        form = ProfileForm(request, POST)

    if form.is_valid():
        pass