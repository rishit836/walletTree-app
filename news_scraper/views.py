from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
    return JsonResponse({"response":"The Api is working."})

def stock_news(request):
    return JsonResponse({"response":"to be done."})