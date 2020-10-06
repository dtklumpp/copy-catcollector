from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Cat
from .forms import Cat_Form, Feeding_Form

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def api(request):
    return JsonResponse({"status": 200})

# index and create
def cats_index(request):
    if request.method == 'POST':
        cat_form = Cat_Form(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('cats_index')
    cats = Cat.objects.all()
    cat_form = Cat_Form()
    context = {'cats': cats, 'cat_form': cat_form}
    return render(request, 'cats/index.html', context)

# show
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = Feeding_Form()
    context = {'cat': cat, 'feeding_form': feeding_form}
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

def add_feeding(request, cat_id):
  import copy
  full_request = copy.copy(request.POST)
  full_request['cat'] = cat_id
  feeding_form = Feeding_Form(full_request)
  if feeding_form.is_valid():
    feeding_form.save()
  return redirect('detail', cat_id=cat_id)

  # print('NOW PRINTING request.post')
  # print(request.POST)
  # full_request = {}
  # full_request['date'] = request.POST['date']
  # full_request['meal'] = request.POST['meal']

  # full_request.cat_id = cat_id
  # print('NOW PRINTING full_request')
  # print(full_request)

  # print('NOW PRINTING feeding form')
  # print(feeding_form)

    # new_feeding = feeding_form.save(commit=False)
    # print('NOW PRINTING new feeding')
    # print(new_feeding)

    # new_feeding.cat_id = cat_id
    # new_feeding.save()

    # feeding_form.save(commit=False)
    # feeding_form.cat_id = cat_id

