from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_employee', views.all_employee, name='all_employee'),
    path('common_friends', views.common_friends, name='common_friends'),
    path('people_details', views.people_details, name='people_details'),
]