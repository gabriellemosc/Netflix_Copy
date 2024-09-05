#url - view - template
from django.urls import path, include
from .views import homepage           #importar a função homepage

urlpatterns = [
   path('',  homepage)
]