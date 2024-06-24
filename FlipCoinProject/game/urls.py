from django.urls import path
from .views import coin_flip_view

urlpatterns = [
    path('', coin_flip_view, name='coin_flip'),
]
