from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api, name='api'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/delete/', views.cats_delete, name='cats_delete'),
    path('cats/<int:cat_id>/edit/', views.cats_edit, name='cats_edit'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('cats/<int:cat_id>/deassoc_toy/<int:toy_id>/', views.deassoc_toy, name='deassoc_toy'),
    path('accounts/signup/', views.signup, name='signup'),
]

