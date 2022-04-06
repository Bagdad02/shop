from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from applications.produkt.models import Product
from applications.produkt.serializers import ProductSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class DeleteUpdateRetrieveView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

