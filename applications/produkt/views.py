from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from applications.produkt.filters import ProductFilter
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

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    # search_fields =['name', 'description'] # ПОИСК
    # filterset_class = ProductFilter
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontins=search))
        return queryset


class DeleteUpdateRetrieveView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ProductSerializer
    permission_classes = [IsAuthor]
    # permission_classes = [IsAuthenticated]
    # pagination_class = None


