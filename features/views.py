from django.shortcuts import render
from rest_framework.permissions import AllowAny


@permission_classes((AllowAny,))
class ProductView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Product.objects.all(), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny,))
class ProductCategoryView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs['id'])
        serializer = self.get_serializer(Product.objects.filter(category=category), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny,))
class CategoryView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Category.objects.all(), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny,))
class ProductFieldView(generics.RetrieveAPIView):
    serializer_class = ProductFieldSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(ProductField.objects.all(), many=True)
        return success_response(serializer.data)
