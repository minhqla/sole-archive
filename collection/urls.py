from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.collection_list, name='collection_list'),
    path('add/', views.collection_create, name='collection_create'),
    path('<int:pk>/', views.collection_detail, name='collection_detail'),
    path('<int:pk>/edit/', views.collection_update, name='collection_update'),
    path('<int:pk>/delete/', views.collection_delete, name='collection_delete'),
]