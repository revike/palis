from rest_framework import serializers

from main.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продуктов"""

    class Meta:
        model = Product
        fields = '__all__'
