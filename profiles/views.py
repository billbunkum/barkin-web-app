from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ProfileForm
from .models import UserProfile

def profile_list(request):
    profile_set = UserProfile.objects.all()
    usernames = []
    for item in profile_set:
        usernames.append(request.user.username)

#    usernames = []
#    profile_set_length = len(profile_set)

#    if profile_set_length > 0:
#        for username in profile_set:
#            name = profile_set.get_username
#            usernames.append(name)
#    import pdb; pdb.set_trace()

#    else:
#        usernames.append("nothing here")
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