import requests
from django.http import HttpResponse
import os

# Daily
def daily(request):
    email = request.GET.get('email')
    if not email:
        return HttpResponse("Missing email parameter", status=400)

    # Replace 'ghl_api_key' with your actual API key
    ghl_api_key = os.environ['GHL_API_KEY']
    url = f'https://rest.gohighlevel.com/v1/contacts/?query={email}&limit=20'
    headers = {'Authorization': f'Bearer {ghl_api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        data = response.json()
        contacts = data.get('contacts', [])
        if not contacts:
            return HttpResponse("Contact not found", status=404)
        
        # Extract contact ID
        contact_id = contacts[0]['id']
        
        # Apply tag
        tag_url = f'https://rest.gohighlevel.com/v1/contacts/{contact_id}/tags'
        tag_payload = {'tags': ['daily']}
        tag_response = requests.post(tag_url, headers=headers, json=tag_payload)
        tag_response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        return HttpResponse("Success! Your preferences have been updated.\nYou can adjust them again by using the frequency links in any recent email that you've received from me.")
    
    except requests.RequestException as e:
        return HttpResponse(f"Request failed: {e}", status=500)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

# Weekly
def weekly(request):
    email = request.GET.get('email')
    if not email:
        return HttpResponse("Missing email parameter", status=400)

    # Replace 'ghl_api_key' with your actual API key
    ghl_api_key = os.environ['GHL_API_KEY']
    url = f'https://rest.gohighlevel.com/v1/contacts/?query={email}&limit=20'
    headers = {'Authorization': f'Bearer {ghl_api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        data = response.json()
        contacts = data.get('contacts', [])
        if not contacts:
            return HttpResponse("Contact not found", status=404)
        
        # Extract contact ID
        contact_id = contacts[0]['id']
        
        # Apply tag
        tag_url = f'https://rest.gohighlevel.com/v1/contacts/{contact_id}/tags'
        tag_payload = {'tags': ['weekly']}
        tag_response = requests.post(tag_url, headers=headers, json=tag_payload)
        tag_response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        return HttpResponse("Success! Your preferences have been updated.\nYou can adjust them again by using the frequency links in any recent email that you've received from me.")
    
    except requests.RequestException as e:
        return HttpResponse(f"Request failed: {e}", status=500)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    



# Opt-out
def opt_out(request):
    email = request.GET.get('email')
    if not email:
        return HttpResponse("Missing email parameter", status=400)

    # Replace 'ghl_api_key' with your actual API key
    ghl_api_key = os.environ['GHL_API_KEY']
    url = f'https://rest.gohighlevel.com/v1/contacts/?query={email}&limit=20'
    headers = {'Authorization': f'Bearer {ghl_api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        data = response.json()
        contacts = data.get('contacts', [])
        if not contacts:
            return HttpResponse("Contact not found", status=404)
        
        # Extract contact ID
        contact_id = contacts[0]['id']
        
        # Apply tag
        tag_url = f'https://rest.gohighlevel.com/v1/contacts/{contact_id}/tags'
        tag_payload = {'tags': ['opt-out']}
        tag_response = requests.post(tag_url, headers=headers, json=tag_payload)
        tag_response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        return HttpResponse("Success! Your preferences have been updated.\nYou can adjust them again by using the frequency links in any recent email that you've received from me.")
    
    except requests.RequestException as e:
        return HttpResponse(f"Request failed: {e}", status=500)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)