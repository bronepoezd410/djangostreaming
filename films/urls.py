from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('genres/<int:genre_id>/', views.categories),
]
