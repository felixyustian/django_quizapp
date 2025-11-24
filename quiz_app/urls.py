from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='quiz_app/login.html'), name='login'), # sesuaikan nama folder template
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]