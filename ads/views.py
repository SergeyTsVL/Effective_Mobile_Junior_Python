from .models import Ad
from .forms import Ad
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def logout_view(request):
    """
    Этот метод выполняет выход пользователя из системы и перенаправляет его на домашнюю страницу.
    """
    logout(request)
    return redirect('templates/home')

def home(request):
    """
    Вызывает страницу home.html .
    """
    return render(request, 'home.html')

def signup(request):
    """
    ызывает страницу для подписи объявлений.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})