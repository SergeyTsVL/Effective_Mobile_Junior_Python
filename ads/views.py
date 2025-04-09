from urllib import request

# from django.core.checks import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib import messages
from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm
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
            ad.status = 'В ожидании'
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
    if ads.status != 'Принято' and ads.user == request.user:      # Проверяет является ли пользователь автором
        if request.method == "POST":
            form = AdForm(request.POST, request.FILES, instance=ads)
            if form.is_valid():
                # ads.user = request.user
                form.save()
                img_obj = form.instance
                # Перенаправляет на страницу с сохраненными исправлениями.
                return redirect('ads:ad_detail', pk=img_obj.pk)
        else:
            # вызов функции которая отобразит в браузере указанный шаблон с данными формы и объявления.
            messages.error(request, 'Вы можете редактировать только свои объявления')
            form = AdForm(instance=ads)
        return render(request, 'ads_ads/edit_ad.html',
                      {'form': form, 'ads': ads})
    return redirect('ads:ad_detail', pk=pk)


@login_required
def create_proposal(request):
    if request.method == "POST":
        form = ExchangeProposalForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            # ad.name = request.user
            ad.status = 'В ожидании'
            ad.save()
            return redirect('ads:create_proposal')
    else:
        form = ExchangeProposalForm()
    return render(request, 'ads_ads/create_proposal.html', {'form': form})

@login_required
def add_proposal(request):
    """
    Вызывает страницу advertisement_list.html.
    """
    # # Фильтрация по частичному совпадению
    # ads = Ad.objects.filter(title__icontains='доставка')
    exc = ExchangeProposal.objects.all()
    return render(request, 'ads_ads/manage_proposal.html', {'exc': exc})









# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.core.exceptions import ObjectDoesNotExist
# from .models import ExchangeProposal
# from .forms import ExchangeProposalForm
#
#
# @login_required
# def create_proposal(request, ad_id):
#     if request.method == 'POST':
#         try:
#             ad = Ad.objects.get(id=ad_id)
#             form = ExchangeProposalForm(request.POST)
#
#             if form.is_valid():
#                 proposal = form.save(commit=False)
#                 proposal.ad_sender = ad
#                 proposal.save()
#
#                 return JsonResponse({
#                     'status': 'success',
#                     'message': 'Предложение создано успешно'
#                 })
#
#         except ObjectDoesNotExist:
#             return JsonResponse({
#                 'status': 'error',
#                 'message': 'Объявление не найдено'
#             }, status=404)
#
#         except Exception as e:
#             return JsonResponse({
#                 'status': 'error',
#                 'message': str(e)
#             }, status=500)
#
#     return render(request, 'ads_ads/create_proposal.html')
#
#
# @login_required
# def manage_proposal(request, proposal_id):
#     try:
#         proposal = ExchangeProposal.objects.get(id=proposal_id)
#
#         if request.method == 'POST':
#             action = request.POST.get('action')
#
#             if action == 'accept':
#                 if proposal.reject():
#                     return JsonResponse({
#                         'status': 'success',
#                         'message': 'Предложение принято'
#                     })
#             elif action == 'reject':
#                 if proposal.reject():
#                     return JsonResponse({
#                         'status': 'success',
#                         'message': 'Предложение отклонено'
#                     })
#             elif action == 'cancel':
#                 if proposal.cancel():
#                     return JsonResponse({
#                         'status': 'success',
#                         'message': 'Предложение отменено'
#                     })
#
#             return JsonResponse({
#                 'status': 'error',
#                 'message': 'Неверное действие'
#             }, status=400)
#
#         return render(request, 'ads_ads/manage_proposal.html', {
#             'proposal': proposal
#         })
#
#     except ObjectDoesNotExist:
#         return JsonResponse({
#             'status': 'error',
#             'message': 'Предложение не найдено'
#         }, status=404)
#
#
