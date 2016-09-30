from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Bark
from .forms import BarkForm


def global_barks_list(request): #shows all user's barks
    ubs = Bark.objects.all()
    user_count = User.objects.count()

    context = {
        "ubs": ubs,
        "user_count": user_count,
    }

    return render(request, "barks/global_barks_list.html", context)

@login_required #shows a specific user's barks
def barks_list(request, id=None):
    if id:
        user = User.objects.get(id=id)
    else:
        user = request.user

    bark_query = user.bark_set.all()

    context = {
        "barks": bark_query,
    }
    return render(request, "barks/barks_list.html", context)

@login_required
def add_bark(request):
    if request.method == "POST":
        form = BarkForm(request.POST)

        if form.is_valid():
            new_bark = form.save(commit=False)
            new_bark.user = request.user

            new_bark.save()
            messages.success(request, "Bark!")
            return redirect('barks:barks_list', id=request.user.id)
    else:
        form = BarkForm()

    context = {
        "form": form,
    }

    return render(request, "barks/bark_form.html", context)