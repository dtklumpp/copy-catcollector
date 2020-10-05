from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cat
from .forms import Cat_Form

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status":200})

def cats_index(request):
    cats = Cat.objects.all()
    cat_form = Cat_Form()
    context = {'cats': cats, 'cat_form':cat_form}
    return render(request, 'cats/index.html', context)

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    context = { 'cat': cat }
    return render(request, 'cats/detail.html', context)