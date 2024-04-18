from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('webhook.urls')),
    path('', include('blog.urls')),
    path('', include('video.urls')),
    path('', include('testimonials.urls')),
    path('', include('contactform.urls')),
    path('', include('properties.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
