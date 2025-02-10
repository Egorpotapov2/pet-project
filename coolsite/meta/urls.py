from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hh', views.bd, name='bd'),
    path('vh', views.hod, name='hod'),
]
