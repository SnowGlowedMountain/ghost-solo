from django.contrib import admin
from .models import Blog, Category, DisplayAd, Offer

admin.site.register(Offer)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)

@admin.register(DisplayAd)
class DisplayAdAdmin(admin.ModelAdmin):
    list_display = ('headline', 'created_at',)
    search_fields = ('headline', 'body',)

@admin.register(Blog)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'created_at', 'display_categories')
    search_fields = ('headline', 'subheadline', 'body',)

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Categories'
