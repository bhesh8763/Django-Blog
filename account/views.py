from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("articles:home")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('articles:home')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("account:register")

        if not gender:
            messages.error(request, "Please select a gender")
            return redirect("account:register")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("account:register")
        
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            phone=phone,
            gender=gender,
            password=password
        )
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect("articles:home")
    
    return render(request, "register.html")