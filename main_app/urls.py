from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api, name='api'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/delete/', views.cats_delete, name='cats_delete'),
]
