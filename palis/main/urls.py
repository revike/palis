from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.ProductListApiView.as_view(), name='products')
]
