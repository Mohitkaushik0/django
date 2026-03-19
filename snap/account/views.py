from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import User
from django.contrib.auth.decorators import login_required

def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('login_success')  # 👈 yahan change
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('login')

    users = User.objects.all()[:20]  # sirf 20 users

    return render(request, 'dashboard.html', {'users': users})




def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success') 

    return render(request, 'signup.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')





@login_required
def login_success(request):
    return render(request, 'login_success.html', {
        'name': request.user.username
    })