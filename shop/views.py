from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from .models import Image
from .forms import NewsLetterForm

def home(request):
    date = dt.date.today()
    images = Image.objects.all()

    return render(request, 'home.html', {'date':date, 'images':images})

def shop(request):

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()

    return render(request, 'shop.html', {'letterForm':form})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message":message})
