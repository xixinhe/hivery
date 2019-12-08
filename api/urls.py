from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_company', views.all_company, name='all_company'),
    path('all_people', views.all_people, name='all_people'),
    path('clear', views.clear, name='clear'),
]