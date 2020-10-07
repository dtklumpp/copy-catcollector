from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Cat, Toy
from .forms import Cat_Form, Feeding_Form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def api(request):
    return JsonResponse({"status": 200})

# --- Cat Views ---

# index and create
def cats_index(request):
    if request.method == 'POST':
        cat_form = Cat_Form(request.POST)
        if cat_form.is_valid():
            # save(commit=False) will just make a copy/instance of the model
            new_cat = cat_form.save(commit=False)
            new_cat.user = request.user
            # save() to the db
            new_cat.save()
            return redirect('cats_index')
    cats = Cat.objects.all()
    cat_form = Cat_Form()
    context = {'cats': cats, 'cat_form': cat_form}
    return render(request, 'cats/index.html', context)

# show
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # [3,1] is what is returned cat.toys.all().values_list('id')
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id')) # get all toys where the cat id is not associated in the jion table
    feeding_form = Feeding_Form()
    context = {'cat': cat, 'feeding_form': feeding_form, 'available_toys': toys_cat_doesnt_have}
    return render(request, 'cats/detail.html', context)

# edit && update
def cats_edit(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  if request.method == 'POST':
    cat_form = Cat_Form(request.POST, instance=cat)
    if cat_form.is_valid():
      cat_form.save()
      return redirect('detail', cat_id=cat_id)
  else:  
    # in form(instance=The object that we pull back from db)
    cat_form = Cat_Form(instance=cat)
  context = {'cat': cat, 'cat_form': cat_form}
  return render(request, 'cats/edit.html', context)

# delete
def cats_delete(request, cat_id):
    Cat.objects.get(id=cat_id).delete()
    return redirect("cats_index")

# --- Feeding Views ---

def add_feeding(request, cat_id):
  feeding_form = Feeding_Form(request.POST)
  if feeding_form.is_valid():
    new_feeding = feeding_form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

# --- Toy Views ---

def assoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    # Cat.objects.get(id=cat_id) return Cat(1) Eldritch
    # Cat.toys returns the join table 
    # table.add -> creates an row in the join table the id provided
    # cat 1 | toy 3 
    return redirect('detail', cat_id=cat_id)

def deassoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('detail', cat_id=cat_id)

# --- Signup View ---

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)