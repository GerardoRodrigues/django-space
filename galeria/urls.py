from django.urls import path

from galeria.views import buscar, hello, image


urlpatterns = [
    path('', hello, name='home'),
    path('imagem/<int:foto_id>', image, name='imagem'),
    path('buscar/', buscar, name='buscar'),
]