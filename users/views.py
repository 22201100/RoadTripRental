from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.models import Purchase


def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_type = request.POST.get("user_type")
        profile_pic = request.FILES.get("profile_pic")  # <-- get the uploaded file

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("signup")

        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            user_type=user_type,
            profile_pic=profile_pic,  # <-- save the image
        )
        user.backend = "users.backends.EmailBackend"
        login(request, user)
        return redirect("home")
    return render(request, "Auth/signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")  # or 'home' or any other page
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    purchases = Purchase.objects.filter(user=request.user).select_related("car")
    return render(request, "Auth/profile.html", {"purchases": purchases})


def welcome_view(request):
    return render(request, "welcome.html")
