from rest_framework import generics

from user.models import User
from user.permissions import IsAnonymous
from user.serializers import RegisterModelSerializer


class RegisterUserApiView(generics.CreateAPIView):
    """Регистрация пользователя"""
    serializer_class = RegisterModelSerializer
    permission_classes = (IsAnonymous,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = False
        user.save()

class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление пользователя"""
    serializer_class = RegisterModelSerializer
    queryset = User.objects.all()
