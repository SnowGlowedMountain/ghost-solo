from django.db import models
from django.utils import timezone

class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
