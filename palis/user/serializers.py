from rest_framework import serializers

from user.models import User


class RegisterModelSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации"""
    telegram_id = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'telegram_id', 'password',)
