from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.properties, name='properties'),
    path('properties/<slug:slug>/', views.property, name='property'),
]