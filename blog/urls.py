from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about_view, name="about"),

    path('<slug:slug>', views.PostDetail.as_view(), name="post-detail")
]