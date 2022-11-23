from rest_framework import generics

from main.models import Product
from main.serializers import ProductSerializer


class ProductListApiView(generics.ListCreateAPIView):
    """Список и создание продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
