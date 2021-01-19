from django.urls import path
from .views import index, commit

urlpatterns = [
    path('', index),
    path('commit/', commit),
]