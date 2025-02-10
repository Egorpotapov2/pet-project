from django.urls import path
from . import views


urlpatterns = [
    path('reg', views.register, name='register'),
    path('log', views.logi, name='logi'),
    path('success/', views.success, name='success')
]
