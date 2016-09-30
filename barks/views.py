from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
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

#@login_required #shows a specific user's barks
def barks_list(request, id=None):
    if id:
        user = User.objects.get(id=id)
        author = user
    else:
        user = request.user
        author = user

    bark_query = user.bark_set.all()

    context = {
        "author": author,
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

@login_required
def edit_bark(request, id=None):
    if id:
        bark = get_object_or_404(Bark, pk=id)

        #probably don't need this as @login_required?
        if bark.user != request.user:
            return HttpResponseForbidden()
    else:
        bark = Bark(request.user)

    form = BarkForm(request.POST, instance = bark) #here's the magic param
    if request.method == "POST":

        if form.is_valid():
            edited_bark = form.save(commit=False)
            edited_bark.user = request.user

            edited_bark.save()
            messages.success(request, "Bark, 'edit'!")
            return redirect('barks:barks_list', id=request.user.id)
    else:
        form = BarkForm()

    context = {
        "form": form,
        "bark": bark,
    }
    return render(request, "barks/edit_bark.html", context)


