from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about_view, name="about"),
    path('blog', views.blog_view, name="blog"),
    path('meme', views.meme_view, name="meme"),
    path('pow', views.pow_view, name="pow"),

    path('project', views.project_view, name="project"),
    path('<slug:slug>', views.PostDetail.as_view(), name="post-detail")
]