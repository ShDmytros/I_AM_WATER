from modeltranslation.translator import register, TranslationOptions
from .models import News, Products


@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')

@register(Products)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')