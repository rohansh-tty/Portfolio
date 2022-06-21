from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post, Meme, Project

posts = Post.objects.all().values()
memes = Meme.objects.all().values()
projects = Project.objects.all().values()


def about_view(request):
    return render(request, "blog/about.html")

def project_view(request):
    return render(request, "blog/projects.html", {'projects': projects})

def blog_view(request):
    return render(request, 'blog/index.html', {'posts': posts})

def home_view(request):
    return render(request, 'blog/home.html')

def meme_view(request):
    return render(request, 'blog/meme.html', {'memes': memes})

def pow_view(request):
    return render(request, 'blog/pow.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

