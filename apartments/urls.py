from django.urls import path
from . import views

urlpatterns = [
    path('', views.apartments_list, name='apartments_list'),
]