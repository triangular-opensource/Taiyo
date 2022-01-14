from django.urls import path

from features.views import ProductFieldView, CategoryView , ProductView , ProductCategoryView

urlpatterns = [
    path("category", CategoryView.as_view(), name="category"),
    path("product", ProductView.as_view(), name="product"),
    path("product/<int:id>", ProductCategoryView.as_view(), name="product-by-category"),
    path("product-field", ProductFieldView.as_view(), name="product-field")
]
