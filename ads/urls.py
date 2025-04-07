from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.add_ad, name='add_ad'),
    path('ad_list/', views.ad_list, name='ad_list'),
    # path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    # path('add/', views.add_advertisement, name='add_advertisement'),
    # path('edit/<int:pk>/', views.edit_advertisement, name='edit_advertisement'),
    # path('delete/<int:pk>/', views.delete_advertisement, name='delete_advertisement'),
]