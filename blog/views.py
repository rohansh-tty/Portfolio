from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

posts = Post.objects.all().values()


def about_view(request):
    return render(request, "blog/about.html")

def project_view(request):
    return render(request, "blog/project.html")


def home_view(request):
    return render(request, 'blog/index.html', {'posts': posts})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

