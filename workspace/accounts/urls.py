from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.persona_login, name='persona_login'),
]