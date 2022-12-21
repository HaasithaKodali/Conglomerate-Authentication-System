from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.logins, name='login'),
    path('login1', views.login1, name='login1'),
    path('login2', views.login2, name='login2'),
    path('login3', views.login3, name='login3'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.log, name='logout'),
]