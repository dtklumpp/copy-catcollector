from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cat

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status":200})

def cats_index(request):
    cats = Cat.objects.all()
    context = {'cats': cats}
    return render(request, 'cats/index.html', context)

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    context = { 'cat': cat }
    return render(request, 'cats/detail.html', context)