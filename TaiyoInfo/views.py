from rest_framework import generics
from rest_framework.views import APIView

from TaiyoInfo.serializers import CategorySerializer, GeneralInfoSerializer, PolicySerializer, AddresSerializer, NewsLetterSerializer, ProductSerializer
from services.mailing import sendNewsEmail

from services.response import success_response, bad_request_response, empty_response, create_response, not_found_response


from TaiyoInfo.models import Category, GeneralInfo, NewsLetter, Addres , Policy, Product



class GeneralInfoView(generics.RetrieveAPIView):
    serializer_class = GeneralInfoSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(GeneralInfo.objects.all(), many=True)
        return success_response(serializer.data)


class PolicyView(generics.RetrieveAPIView):
    serializer_class = PolicySerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Policy.objects.all(), many=True)
        return success_response(serializer.data)


class AddressView(generics.RetrieveAPIView):
    serializer_class = AddresSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Addres.objects.all(), many=True)
        return success_response(serializer.data)


class NewsLetterView(generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = NewsLetterSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(NewsLetter.objects.all(), many=True)
        return success_response(serializer.data)


class CategoryView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Category.objects.aa(), many=True)
        return success_response(serializer.data)


class ProductView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Product.objects.aa(), many=True)
        return success_response(serializer.data)
