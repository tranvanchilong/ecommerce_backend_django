from django.urls import path, include
# from .views import LatestProductsList
from product import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('categorys/', views.CategorysList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]