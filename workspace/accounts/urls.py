from django.contrib import auth
from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.persona_login, name='persona_login'),
    path('logout', auth.logout, name='logout'),
]