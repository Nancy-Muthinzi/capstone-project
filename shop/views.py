from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image
from .forms import NewsLetterForm


def home(request):
    date = dt.date.today()
    images = Image.objects.all()

    return render(request, 'home.html', {'date': date, 'images': images})


def about(request):
    return render(request, 'about.html')


def shop(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            HttpResponseRedirect('shop')
    else:
        form = NewsLetterForm()

    return render(request, 'shop.html', {'letterForm':form})

def contact(request):

    return render(request, 'contact.html')    

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message":message})
