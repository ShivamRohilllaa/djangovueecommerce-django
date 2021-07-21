from django.urls import path, include
from ecom_product import views

urlpatterns = [
    path('latest-products/', views.LatestProductSerializer.as_view(), name='lastest'),
    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetailSerializer.as_view(), name='products'),
    path('category/<slug:category_slug>', views.CategoryDetailSerializer.as_view(), name='category'),
    
]
