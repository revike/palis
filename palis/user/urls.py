from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterUserApiView.as_view(), name='register'),
    path('user/<int:pk>/', views.UserApiView.as_view(), name='user'),
]
