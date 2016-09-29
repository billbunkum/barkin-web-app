from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Bark
from .forms import BarkForm


def global_barks_list(request):
    user_query = User.objects.all()
    usernames = []
    for item in user_query:
        x = getattr(item, 'username')
        usernames.append(x)

    ubs = {}
    for i in user_query:
        x = i.username
        y = i.bark_set.all()
        ubs[x] = y

    context = {
        "usernames": usernames,
        "ubs": ubs,
    }
#    import pdb; pdb.set_trace()
    return render(request, "barks/global_barks_list.html", context)

def barks_list(request, id):
    return render(request, "barks/barks_list.html")

@login_required
def add_bark(request):
    if request.method == "POST":
        form = BarkForm()
    else:
        form = BarkForm()

    context = {
        "form": form,
    }

    return render(request, "barks/bark_form.html", context)