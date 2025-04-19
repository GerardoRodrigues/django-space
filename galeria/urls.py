from django.urls import path

from galeria.views import hello, space


urlpatterns = [
    path('', hello),
    path('space/', space)
]