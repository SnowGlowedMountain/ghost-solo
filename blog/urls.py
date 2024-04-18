from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogs, name='blogs'),
    path('blog/<slug:slug>/', views.blog, name='blog'),
]
