from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>/', views.PostDetal, name='post_detal'),
    path('auth', views.Auth, name='login'),
]