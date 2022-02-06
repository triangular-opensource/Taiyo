from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import generics
from features.serializer import *
from features.models import *
from services.response import success_response, bad_request_response


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
        sub_category = SubCategory.objects.get(id=kwargs['id'])
        serializer = self.get_serializer(Product.objects.filter(sub_category=sub_category), many=True)
        return success_response(serializer.data)


@permission_classes((AllowAny,))
class CategoryView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Category.objects.all(), many=True)
        return success_response(serializer.data)




@permission_classes((AllowAny,))
class SubCategoryView(generics.RetrieveAPIView):
    serializer_class = SubCategorySerializer
    def get(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs['id'])
        serializer = self.get_serializer(SubCategory.objects.filter(category=category), many=True)
        return success_response(serializer.data)










