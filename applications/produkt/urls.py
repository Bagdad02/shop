from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.produkt.views import *

router = DefaultRouter()
router.register('', ProductViewSet)



urlpatterns = [
    # path('', ProductViewSet.as_view({'get': 'list'})),
    # path('', ListCreateView.as_view()),

    path('category/', CategoryListCreateView.as_view()),
    path('category/<str:slug>/', CategoryRetriveDeleteUpdateView.as_view()),
    path('',include(router.urls)),
    # path('<int:pk>/', DeleteUpdateRetrieveView.as_view())

]