from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
def login_view(request):
    return render(request, "accounts/login.html")

def registerAccount(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})