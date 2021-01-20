from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def blog_api(request):
    data = {
        "test": "test data"
    }
    return JsonResponse(data)