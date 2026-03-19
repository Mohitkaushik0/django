from django.urls import path
from .views import signup_view, login_view, dashboard, success_view, login_success

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('success/', success_view, name='success'),
    path('login-success/', login_success, name='login_success'),
]