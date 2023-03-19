from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product import views
from .views import ReviewViewSet

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/',views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/',views.CategoryDetail.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('products/<slug:product_slug>/reviews', views.ReviewList.as_view()),
    path('',include(router.urls))
]


