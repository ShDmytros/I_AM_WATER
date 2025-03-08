from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("slides/", views.SlidesView.as_view(), name="slides"),
    path("news/", views.NewsView.as_view(), name="news"),
    path("news/<slug:slug>/", views.NewsDetailViews.as_view(), name="news_detail"),
    path("shop/", views.ShopView.as_view(), name="shop"),
    path("shop/<slug:slug>/", views.ProductView.as_view(), name="product_menu"),
]