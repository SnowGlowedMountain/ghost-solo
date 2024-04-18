from django.shortcuts import render
from .models import Testimonial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def testimonial(request, page=1):
    testimonials = Testimonial.objects.all()
    
    # Pagination logic
    items_per_page = int(request.GET.get('itemsPerPage', 8))
    paginator = Paginator(testimonials, items_per_page)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'testimonials': page.object_list,
        'total': paginator.count,
        'page': page.number,
        'total_pages': paginator.num_pages,
    }
    return render(request, 'pages/testimonials.html', context)

def testimonials(request):
    testimonials = Testimonial.objects.all()
    
    context = {
        'testimonials': testimonials,
        'total': len(testimonials),
    }
    return render(request, 'pages/testimonials.html', context)

def get_testimonials():
    testimonials = Testimonial.objects.all()
    return {'testimonials': testimonials}
