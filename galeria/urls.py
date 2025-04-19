from django.urls import path

from galeria.views import hello, image


urlpatterns = [
    path('', hello, name='home'),
    path('imagem/', image, name='imagem')
]