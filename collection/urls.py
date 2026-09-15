from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('sneakers/add/', views.sneaker_create, name='sneaker_create'),
    path('collection/', views.collection_list, name='collection_list'),
    path('collection/add/', views.collection_create, name='collection_create'),
    path('collection/<int:pk>/', views.collection_detail, name='collection_detail'),
    path('collection/<int:pk>/edit/', views.collection_update, name='collection_update'),
    path('collection/<int:pk>/delete/', views.collection_delete, name='collection_delete'),
]