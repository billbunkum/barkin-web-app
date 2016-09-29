from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])

            new_user.save()
            messages.success(request, 'Congrats! You now exist.')
#messages currently ONLY displays @ admin/ when logging in...how to change?

            return redirect('barks:barks_list')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/register.html", context)