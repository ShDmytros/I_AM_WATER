from django.contrib import admin
from .models import News, Products
from .translation import News, Products
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ("name", "short_description", "description")
    list_display_links = ("name",)

@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    list_display = ("name", "description")
    list_display_links = ("name",)