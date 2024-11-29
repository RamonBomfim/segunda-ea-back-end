from django.urls import path
from .views import produto_new

urlpatterns = [
    path('', produto_new, name='produto_new'),  # Rota para cadastrar novo produto
]