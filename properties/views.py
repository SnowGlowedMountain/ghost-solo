# views.py
from django.shortcuts import render, get_object_or_404
from .models import Property, PropertyImage
from django.contrib.humanize.templatetags.humanize import intcomma

def properties(request):
    properties = Property.objects.all()
    for property in properties:
        images = PropertyImage.objects.filter(property=property)
        if images:
            property.first_image = images.first().image.url
        else:
            property.first_image = None

    return render(request, 'pages/properties.html', {'properties': properties})

def property(request, slug):
    property_instance = get_object_or_404(Property, slug=slug)
    images = PropertyImage.objects.filter(property=property_instance)
    image_urls = [image.image.url for image in images]

    property_data = {
        "name": property_instance.name,
        "built_in": property_instance.built_in,
        "slug": property_instance.slug,
        "address": property_instance.address,
        "unit_number": property_instance.unit_number,
        "city": property_instance.city,
        "state": property_instance.state,
        "postal_code": property_instance.postal_code,
        "price": str(property_instance.price),
        "description": property_instance.description,
        "tag": property_instance.tag,
        "bedrooms": property_instance.bedrooms,
        "bathrooms": str(property_instance.bathrooms),
        "year_built": property_instance.year_built,
        "interior_sqft": property_instance.interior_sqft,
        "lot_size": property_instance.lot_size,
        "youtube_video_id": property_instance.youtube_video_id,
        "images": image_urls,
        "priority": property_instance.priority,
    }

    return render(request, 'pages/property_detail.html', {'property': property_data})


from .models import Property, PropertyImage
from django.contrib.humanize.templatetags.humanize import intcomma

def get_featured_properties():
    properties = Property.objects.all().order_by('-price')[:10]
    formatted_properties = []
    for property in properties:
        # Fetch all images for the property
        images = PropertyImage.objects.filter(property=property)
        image_urls = [image.image.url for image in images]

        # Format the price
        if str(property.price).endswith('.00'):
            price = int(property.price)
        else:
            price = round(property.price, 2)

        # Add comma formatting
        formatted_price = f"${intcomma(price)}"

        # Append the formatted property with images
        formatted_properties.append({
            'name': property.name,
            'address': property.address,
            'price': formatted_price,
            'description': property.description,
            'images': image_urls,  # Now this is a list of URLs
            'slug': property.slug
        })

    return formatted_properties
