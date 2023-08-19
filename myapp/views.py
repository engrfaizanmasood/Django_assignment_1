from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def detail(request):
    return render(request, 'myapp/detail.html')