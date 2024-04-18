from django.shortcuts import render, get_object_or_404
from .models import Blog, DisplayAd, Offer
# Blogs
def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    ads = DisplayAd.objects.all() 
    context = {'blogs': blogs, 'page_name': 'Blogs', 'ads': ads}
    return render(request, 'pages/blogs.html', context)

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog': blog, 'page_name': blog.headline}
    return render(request, 'pages/blog.html', context)

# # Offers
# def offer(request, slug):
#     offer = get_object_or_404(Offer, slug=slug)
#     context = {'offer': offer, 'page_name': offer.headline}
#     return render(request, 'pages/offer.html', context)