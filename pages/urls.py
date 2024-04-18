from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('properties/', views.properties, name='properties'),
    # path('properties/<slug:property_slug>/', views.property_detail, name='property_detail'),
    path('about/', views.about, name='about'),
    # path('testimonials/', views.testimonials, name='testimonials'),
    # path('videos/', views.videos, name='videos'),
    # path('articles/', views.articles, name='articles'),
    # path('articles/<slug:slug>/', views.article, name='article'),
    # path('contact/', views.contact, name='contact'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
