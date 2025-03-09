from django.db import models
from django.urls import reverse
from datetime import date
import os

# Create your models here.
class News(models.Model):
    name = models.CharField("Наза статті", max_length=70)

    short_description = models.CharField("Короткий опис", max_length=70, default="")

    givenFrom = models.CharField("Звідки взято інформацію / Хто написав", max_length=160, default="")
    givenFromUrl = models.CharField("Посилання на статтю", max_length=160, default="", null=True, blank=True)

    description = models.TextField("Опис")

    date = models.DateField("Дата публікації", default=date.today)
    url = models.SlugField(max_length=160)
    image = models.ImageField("Зображення", upload_to="posters_of_news/", default="")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        
    def delete(self, *args, **kwargs):
        """Видаляє зображення при видаленні статті"""
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        try:
            old_article = News.objects.get(pk=self.pk)
            if old_article.image and old_article.image != self.image:
                if os.path.isfile(old_article.image.path):
                    os.remove(old_article.image.path)
        except News.DoesNotExist:
            pass
    
        super().save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField("Назва товару", max_length=70)
    description = models.TextField("Опис")

    url = models.SlugField(max_length=160)

    price = models.FloatField("Ціна", default=0, help_text="Вказувати суму в доларах")

    image = models.ImageField("Зображення", upload_to="products/", default="")
    
    is_avaible = models.BooleanField("Чи в наявності", default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_menu", kwargs={"slug": self.url })

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
    
    def delete(self, *args, **kwargs):
        """Видаляє зображення при видаленні статті"""
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            old_article = Products.objects.get(pk=self.pk)
            if old_article.image and old_article.image != self.image:
                if os.path.isfile(old_article.image.path):
                    os.remove(old_article.image.path)
        except Products.DoesNotExist:
            pass
    
        super().save(*args, **kwargs)