from django.urls import path

from features.views import CategoryView , ProductView , ProductCategoryView , SubCategoryView

urlpatterns = [
    path("category", CategoryView.as_view(), name="category"),
    path("sub-category/<int:id>", SubCategoryView.as_view(), name="sub-categgory-by-category"),
    path("product/<int:id>", ProductCategoryView.as_view(), name="product-by-sub-category"),
    ##extra
    path("product", ProductView.as_view(), name="product"),
]
