from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h2>This is Blog HomePage.</h2>")
    

def about_view(request):
    return HttpResponse("<h2>This is About Page</h2>")