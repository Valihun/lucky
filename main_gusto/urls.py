from django.urls import path
from .views import main

urlspatterns = [
    path('', main, name='main'),
]