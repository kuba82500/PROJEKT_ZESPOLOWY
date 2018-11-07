from django.urls import path
from .views import account_user, main_page
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('main/', main_page, name='main_page'),
    path('profile/', account_user, name='profile'),
]
