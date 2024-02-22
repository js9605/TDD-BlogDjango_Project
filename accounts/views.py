from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegistrationForm


def register_user(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            print("DEBUG: form is valid for register_user()")
            form.save()

            return redirect(reverse('login_page'))
        else:
            print("DEBUG: form is invalid for register_user()")

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_page(request):
    return render(request, "accounts/login.html")
