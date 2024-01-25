from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm



def adminsignup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('adminlogin')   
    else:
        form = UserCreationForm()

    return render(request, 'adminsignup.html', {'form': form})
def adminlogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}! You are now logged in.")
                return redirect('dashboard')  # Redirect to your dashboard view
            else:
                messages.error(request, "You do not have superuser privileges.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'adminlogin.html')  # Replace 'login.html' with the actual template for your login page

@login_required
def dashboard_view(request):
    return render(request, 'admindashboard.html')  # Replace 'dashboard.html' with the actual template for your dashboard

