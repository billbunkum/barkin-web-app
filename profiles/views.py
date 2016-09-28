from django.shortcuts import render

def profile_list(request):
    return render(request, "profiles/profile_list.html")

def user_profile(request):
    return render(request, "core/profile.html")