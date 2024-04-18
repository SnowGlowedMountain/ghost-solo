from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_video_id', 'order', 'created_at')
    search_fields = ('title', 'youtube_video_id')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}