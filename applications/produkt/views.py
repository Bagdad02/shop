from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from applications.produkt.models import Product
from applications.produkt.permission import IsAdmin, IsAuthor
from applications.produkt.serializers import ProductSerializer


#pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class ListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = None
    pagination_class = LargeResultsSetPagination


class DeleteUpdateRetrieveView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ProductSerializer
    permission_classes = [IsAuthor]
    # permission_classes = [IsAuthenticated]
    # pagination_class = None


