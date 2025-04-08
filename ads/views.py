from urllib import request
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Ad
from .forms import AdForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
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
    добавлении данных, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
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

@login_required
def ad_list(request):
    """
    Вызывает страницу advertisement_list.html.
    """
    # # Фильтрация по частичному совпадению
    # ads = Ad.objects.filter(title__icontains='доставка')
    ads = Ad.objects.all()
    return render(request, 'ads_ads/ad_list.html', {'ads': ads})


class SearchResultsView(ListView):
    model = Ad
    template_name = 'ads_ads/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Ad.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list

class HomePageView(TemplateView):
    template_name = 'ads_ads/search.html'


def ad_detail(request, pk):
    """
    Вызывает страницу ad_detail.html.
    """
    ad = Ad.objects.get(pk=pk)
    return render(request, 'ads_ads/ad_detail.html', {'ad': ad})

@login_required
def delete_ad(request, pk):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", после чего удаляет
    объявление и возвращается в окно объявления.
    :param request:
    :param pk:
    :return:
    """
    ad = Ad.objects.get(pk=pk)
    if ad.status != 'Принято':
        if request.method == "POST":
            ad.delete()
            return redirect('ads:ad_list')
        else:
            None
        return render(request, 'ads_ads/delete_ad.html', {'ad': ad})
    else:
        return redirect('ads:ad_list')

@login_required    # Проверяет регистрацию пользователя
def edit_ad(request, pk):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", обрабатывает
    данные формы, если все поля заполнены полностью, корректны и содержат все необходимые данные. Затем, при
    редактировании, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
    не было, то возвращаемся к предыдущей странице без изменений.
    :param request:
    :param pk:
    :return:
    """
    ads = Ad.objects.get(pk=pk)
    if ads.status != 'Принято':
        if request.method == "POST" and ads.user != request.user:   # Проверяет является ли пользователь автором
            form = AdForm(request.POST, request.FILES, instance=ads)
            if form.is_valid():
                form.save()
                img_obj = form.instance
                # Перенаправляет на страницу с сохраненными исправлениями.
                return redirect('ads:ad_detail', pk=img_obj.pk)
        else:
            # вызов функции которая отобразит в браузере указанный шаблон с данными формы и объявления.
            form = AdForm(instance=ads)
        return render(request, 'ads_ads/edit_ad.html',
                      {'form': form, 'ads': ads})
    return redirect('ads:ad_detail', pk=pk)


