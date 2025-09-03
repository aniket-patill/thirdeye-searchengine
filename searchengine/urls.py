from django.urls import path
from .register import register_user
from .login import login_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]