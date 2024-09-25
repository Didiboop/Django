from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import custom_logout , CustomLoginView

urlpatterns = [
    path('contact/', views.contact, name='contact'), 
    path('', views.homepage, name='homepage'),
    path('services/', views.services, name='services'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('contact/login/', views.CustomLoginView.as_view(), name='login'),
   path('logout/', custom_logout, name='logout'),
]