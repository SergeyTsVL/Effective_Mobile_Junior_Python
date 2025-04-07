from .models import Ad
from .forms import AdForm
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
    return redirect('home')

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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required  # Проверяет регистрацию пользователя
def add_ad(request):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", обрабатывает
    данные формы, если все поля заполнены полностью, корректны и содержат все необходимые данные. Затем, при
    обавлении данных, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
    не было, то возвращаемся к предыдущей странице без изменений.
    """
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            # ad.name = request.user
            ad.status = 'заявка создана'
            ad.save()
            return redirect('ads:add_ad')
    else:
        form = AdForm()
    return render(request, 'ads_ads/add_ad.html', {'form': form})

def ad_list(request):
    """
    Вызывает страницу advertisement_list.html.
    """
    ads = Ad.objects.all()
    return render(request, 'ads_ads/ad_list.html', {'ads': ads})