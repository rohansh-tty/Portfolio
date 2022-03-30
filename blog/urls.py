from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='blog-home'), 
    path('about/', views.about_view, name='blog-about')
]