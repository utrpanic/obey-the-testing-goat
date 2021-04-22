from django.urls import path, include

import accounts.views

urlpatterns = [
    path('login', accounts.views.login, name='login'),
    path('logout', accounts.views.logout, name='logout'),
]
