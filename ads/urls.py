from django.urls import path
from . import views
from .views import SearchResultsView, HomePageView

# from .views import AdListView

app_name = 'ads'
urlpatterns = [
    path('', views.add_ad, name='add_ad'),
    path('ad_list/', views.ad_list, name='ad_list'),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('search/', HomePageView.as_view(), name='search'),
    path('edit/<int:pk>/', views.edit_ad, name='edit_ad'),
    path('delete/<int:pk>/', views.delete_ad, name='delete_ad'),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    # path('edit/<int:pk>/', views.edit_advertisement, name='edit_advertisement'),
    # path('delete/<int:pk>/', views.delete_advertisement, name='delete_advertisement'),
]