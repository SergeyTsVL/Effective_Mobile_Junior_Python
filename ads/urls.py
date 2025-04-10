from django.urls import path

from django.conf import settings
from . import views
from .views import SearchResultsView, HomePageView
from django.conf.urls.static import static


app_name = 'ads'

urlpatterns = [
    path('', views.add_ad, name='add_ad'),
    path('ad_list/', views.ad_list, name='ad_list'),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('search/', HomePageView.as_view(), name='search'),
    path('edit/<int:pk>/', views.edit_ad, name='edit_ad'),
    path('delete/<int:pk>/', views.delete_ad, name='delete_ad'),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    path('create_proposal', views.create_proposal, name='create_proposal'),
    path('add_proposal', views.add_proposal, name='add_proposal'),
    path('profile/', views.logout_view, name='logout_view'),
    path('edit_exc/<int:pk>/', views.edit_exc, name='edit_exc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)