from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import News, Products
# Create your views here.


# class MainView(View):
#     def get(self, request):
#         news = News.objects.all()
#         return render(request, "water_site/index.html", {"news_list": news[::-1]})

class MainView(ListView):
    model = News
    queryset = News.objects.all()
    template_name =  "water_site/index.html"

class SlidesView(View):
    def get(self, request):
        return render(request, "water_site/slides_styles.html")

class NewsView(ListView):
    model = News
    queryset = News.objects.order_by('-date')
    template_name =  "water_site/news.html"

class NewsDetailViews(DetailView):
    model = News
    slug_field = "url"
    template_name =  "water_site/news_detail.html"

class ShopView(ListView):
    model = Products
    queryset = Products.objects.all()
    template_name =  "water_site/shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context["object_list"]:
            product.price = "{:.2f}".format(product.price).replace(",", ".")
        return context

class ProductView(DetailView):
    model = Products
    slug_field = "url"
    template_name =  "water_site/product_menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context["object"]
        product.price = "{:.2f}".format(product.price).replace(",", ".")
        return context