from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class DisplayAd(models.Model):
    thumbnail = models.ImageField(upload_to='static/ads/', blank=True, null=True)
    headline = models.CharField(max_length=200)
    body = RichTextField()
    cta_button_text = models.CharField(max_length=50)
    cta_button_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Blog(models.Model):
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='static/thumbnails/', blank=True, null=True)
    date = models.DateField(default=timezone.now)
    body = RichTextField()
    category = models.ManyToManyField(Category, related_name='blogs', blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    selected_ads = models.ManyToManyField(DisplayAd, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    youtube_video_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super(Blog, self).save(*args, **kwargs)

class Offer(models.Model):
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='offers/thumbnails/', blank=True, null=True)
    video_url = models.URLField(max_length=200, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    body = RichTextField()
    custom_code = models.TextField(blank=True, null=True)
    cta_button_text = models.CharField(max_length=50, null=True, blank=True)
    cta_button_link = models.URLField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super(Offer, self).save(*args, **kwargs)