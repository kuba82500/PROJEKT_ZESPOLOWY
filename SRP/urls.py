from django.urls import path
from .views import account_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('account/', account_user),
]
