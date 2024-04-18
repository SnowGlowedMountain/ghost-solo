from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=20)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
