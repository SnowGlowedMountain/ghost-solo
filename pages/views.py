import requests
from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.dateparse import parse_datetime
from operator import itemgetter
from django.views.decorators.cache import cache_page
from testimonials.models import Testimonial
from testimonials.views import get_testimonials
from properties.views import get_featured_properties


# This is for formating bathrooms to 3, 3.25, 3.5, and 3.75
def format_bathrooms(bathroom_count):
    try:
        # Convert to a float and round to two decimal places
        bathrooms = float(bathroom_count)
        if bathrooms.is_integer():
            return int(bathrooms)
        return round(bathrooms, 2) 
    except ValueError:
        return bathroom_count

# Home
# @cache_page(60 * 15)  # Cache valid for 15 minutes
def home(request):

   # Use local function to fetch properties
    properties_data = get_featured_properties()

    # Fetch testimonials from your Django app
    testimonials_data = get_testimonials()  # Assume this function is defined as suggested before

    # Pass data to the template
    return render(request, 'pages/index.html', {
        'featured': properties_data,
        'testimonials': testimonials_data['testimonials']
    })
# # Properties
# @cache_page(60 * 15)  # Cache valid for 15 minutes
# def properties(request):
#     base_url = "https://parkplaceapi.us/api/properties/austinhomolka/all/"
#     response = requests.get(base_url)
#     properties_data = response.json() if response.status_code == 200 else []

#     for property in properties_data:
#         detail_url = f"https://parkplaceapi.us/api/properties/austinhomolka/{property['slug']}/"
#         detail_response = requests.get(detail_url)
#         detail_data = detail_response.json() if detail_response.status_code == 200 else {}

#         if detail_data:
#             property.update(detail_data)
#             property['first_image'] = property['images'][0] if 'images' in property and property['images'] else None

#         # Format the bathrooms field
#         if 'bathrooms' in property:
#             property['bathrooms'] = format_bathrooms(property['bathrooms'])

#     return render(request, 'pages/properties.html', {
#         'properties': properties_data
#     })


# # Property page
# def property_detail(request, property_slug):
#     detail_url = f"https://parkplaceapi.us/api/properties/austinhomolka/{property_slug}/"
#     response = requests.get(detail_url)
#     if response.status_code == 200:
#         property_data = response.json()
#     else:
#         raise Http404("Property does not exist")

#     # Format the bathrooms data before passing to the template
#     if 'bathrooms' in property_data:
#         property_data['bathrooms'] = format_bathrooms(property_data['bathrooms'])

#     # Fetch additional data if necessary (e.g., member data)
#     member_url = "https://parkplaceapi.us/api/member/austinhomolka"
#     member_response = requests.get(member_url)
#     member_data = member_response.json() if member_response.status_code == 200 else {}

#     return render(request, 'pages/property_detail.html', {
#         'property': property_data,
#         'member': member_data,
#     })

# About page
# @cache_page(60 * 15)  # Cache valid for 15 minutes
def about(request):
    return render(request, 'pages/about.html')

# # Testimonials page
# @cache_page(60 * 15)  # Cache valid for 15 minutes
# def testimonials(request):
#      # Fetch testimonials data
#     testimonials_url = "https://parkplaceapi.us/api/testimonials/austinhomolka"
#     testimonials_response = requests.get(testimonials_url)
#     testimonials_data = testimonials_response.json() if testimonials_response.status_code == 200 else {}
#     # Pass data to the template
#     return render(request, 'pages/testimonials.html', {
#         'testimonials': testimonials_data.get('testimonials', [])
#     })

# # Videos page
# @cache_page(60 * 15)  # Cache valid for 15 minutes
# def videos(request):
#     # Fetch videos data
#     videos_url = "https://parkplaceapi.us/api/videos/austinhomolka/"
#     videos_response = requests.get(videos_url)
#     if videos_response.status_code == 200:
#         videos_data = videos_response.json().get('videos', [])
#     else:
#         raise Http404("Videos data not available")

#     # Pass data to the template
#     return render(request, 'pages/videos.html', {
#         'videos': videos_data
#     })

# # Articles page
# logger = logging.getLogger(__name__)

# # Articles page
# def get_articles_from_api(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         articles_data = response.json().get('articles', [])
#         published_articles = [article for article in articles_data if article['status'] == 'published']
#         sorted_articles = sorted(published_articles, key=itemgetter('published_date'), reverse=True)
#         return sorted_articles, response.elapsed.total_seconds()
#     else:
#         return None, None

# @cache_page(60 * 15)  # Cache valid for 15 minutes
# def articles(request):
#     articles_url = "https://parkplaceapi.us/api/articles/austinhomolka/"
#     sorted_articles = []
#     elapsed_time = None

#     with ThreadPoolExecutor() as executor:
#         future = executor.submit(get_articles_from_api, articles_url)
#         sorted_articles, elapsed_time = future.result()

#     if sorted_articles is None:
#         raise Http404("Articles data not available")

#     if elapsed_time:
#         logger.info(f"Published articles sorted successfully in {elapsed_time} seconds")

#     return render(request, 'pages/articles.html', {
#         'articles': sorted_articles
#     })


# # Article page
# def article(request, slug):
#     article_url = f"https://parkplaceapi.us/api/articles/austinhomolka/{slug}/"
#     response = requests.get(article_url)
#     if response.status_code == 200:
#         article_data = response.json()
#         # Parse the created_at field to ensure it's a datetime object
#         article_data['created_at'] = parse_datetime(article_data['created_at'])

#         # Parse display ad and category if they exist in the JSON response
#         display_ad = article_data.get('display_ad', {})
#         category = article_data.get('category', {})

#     else:
#         raise Http404("Article not found")

#     return render(request, 'pages/article.html', {
#         'article': article_data,
#         'display_ad': display_ad,
#         'category': category
#     })

# # Contact
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Prepare data for API submission
#             form_data = {
#                 'full_name': form.cleaned_data['full_name'],
#                 'subject': form.cleaned_data['subject'],
#                 'phone': form.cleaned_data['phone'],
#                 'email': form.cleaned_data['email'],
#                 'message': form.cleaned_data['message'],
#             }
            
#             # API endpoint
#             api_url = f"https://parkplaceapi.us/api/contactform/austinhomolka/"
            
#             # Make the POST request to the external API
#             response = requests.post(api_url, json=form_data)
#             if response.status_code == 200:
#                 # Redirect to a new URL or show a success message
#                 return redirect('home')
#             else:
#                 # Handle API errors here
#                 form.add_error(None, 'Error submitting form. Please try again.')

#     else:
#         form = ContactForm()

#     return render(request, 'pages/contact.html', {'form': form})


# Terms of Service page
def terms_of_service(request):
    return render(request, 'pages/terms_of_service.html')

# Privacy Policy page
def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')