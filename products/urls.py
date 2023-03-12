from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(),
         name='product-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(),
         name='category-detail'),
    path('products/<int:product_pk>/files/',
         views.FileListView.as_view(), name='file-list'),
    path('products/<int:product_pk>/files/<int:pk>/',
         views.FileDetailView.as_view(), name='file-detail'),
]
