from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import ContactFormForm
import logging
import requests

logger = logging.getLogger(__name__)

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            logger.info(f"New contact form saved: {new_contact.id}")

            # Call send_mailgun_email function here
            response = send_mailgun_email('austin@mg.austinhomolka.com', form.cleaned_data)
            if response.status_code == 200:
                logger.info("Email sent successfully")
            else:
                logger.error(f"Failed to send email: {response.status_code} {response.text}")

            # Redirect to the 'home' named URL, which should render 'pages/index.html'
            return redirect('home')
        else:
            logger.error(f"Form validation errors: {form.errors}")
            return HttpResponseBadRequest("Invalid form data")
    else:
        form = ContactFormForm()
        return render(request, 'pages/contact.html', {'form': form})






def send_mailgun_email(to_email, form_data):
    api_key = '038ff96d2321faeafa9b8b8e62280281-19806d14-e3e96da6'
    domain = 'mg.austinhomolka.com'
    sender = 'austin@mg.austinhomolka.com'

    email_body = f"""
    You have a new lead. Here are the details!
    
    Name: {form_data.get('full_name')}
    Subject: {form_data.get('subject')}
    Phone: {form_data.get('phone')}
    Email: {form_data.get('email')}
    Message: {form_data.get('message')}
    """

    url = f"https://api.mailgun.net/v3/{domain}/messages"
    auth = ("api", api_key)
    data = {
        "from": sender,
        "to": to_email,
        "subject": "You have a new lead",
        "text": email_body
    }

    response = requests.post(url, auth=auth, data=data)
    if response.status_code != 200:
        logger.error(f"Failed to send email: {response.status_code} {response.text}")
    else:
        logger.info("Email sent successfully")

    return response
