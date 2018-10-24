from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from .models import Image


def home(request):
    date = dt.date.today()
    images = Image.objects.all()

    return render(request, 'home.html', {'date':date, 'images':images})

def shop(request):

    return render(request, 'shop.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message":message})
