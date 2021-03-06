from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet

from applications.produkt.filters import ProductFilter
from applications.produkt.models import Product, Rating, Category
from applications.produkt.permission import IsAdmin, IsAuthor
from applications.produkt.serializers import ProductSerializer, RatingSerializers, CategorySerializers


#pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filter_fields = ['category']
    filterset_class = ProductFilter
    ordering_fields = ['id', 'price']
    search_fields = ['name', 'description']

    def get_permissions(self):
        print(self.action)
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'rating':
            permission = [IsAuthenticated]

        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    @action(methods=['POST'], detail=True)
    def rating(self,request,pk): # http://localhost:8000/product/id_product/rating/
        serializer = RatingSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = Rating.objects.get(product=self.get_object(), owner=request.user)
            obj.rating = request.data['rating']
        except Rating.DoesNotExist:
            obj = Rating(owner=request.user, product=self.get_object(), rating=request.data['rating'])
        obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]


class CategoryRetriveDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]


#
# class ListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     # permission_classes = None
#     pagination_class = LargeResultsSetPagination
#
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['category', 'price']
#     # search_fields =['name', 'description'] # ??????????
#     # filterset_class = ProductFilter
#     ordering_fields = ['id']
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search = self.request.query_params.get('search')
#         if search:
#             queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontins=search))
#         return queryset
#
#
# class DeleteUpdateRetrieveView(RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = ProductSerializer
#     permission_classes = [IsAuthor]
#     # permission_classes = [IsAuthenticated]
#     # pagination_class = None
#


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# #
# class ProductViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductViewSet(ViewSet):
#     pass
#     def list(self,request):
#         pass
#     def create(self):
#         pass
#     def retrieve(self):
#         pass
#     def update(self):
#         pass


