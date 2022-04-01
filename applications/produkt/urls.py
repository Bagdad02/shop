from django.urls import path

from applications.produkt.views import *

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('<int:pk>/', DeleteUpdateRetrieveView.as_view())

]