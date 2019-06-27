from django.shortcuts import render

import products


def home(request):
    return render(request, 'products/home.html')
