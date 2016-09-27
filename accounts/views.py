from django.shortcuts import render, redirect

from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])

            new_user.save()
            messages.success(request, 'Congrats! You now exist.')

            return redirect('core:index')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/register.html", context)