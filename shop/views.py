from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image, Blog
from .forms import NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from .models import Cart, JewelOrder, Jewel


def home(request):
    date = dt.date.today()
    images = Image.objects.all()

    return render(request, 'home.html', {'date': date, 'images': images})


def about(request):
    return render(request, 'about.html')

# @login_required(login_url='/accounts/login/')
def shop(request):
    images = Image.objects.all()

    return render(request, 'shop.html', {'images':images})


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    blog = Blog.objects.all()
    
    return render(request, 'blog.html', {'blog':blog})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def add_to_cart(request,jewel_id):
    jewel = get_object_or_404(Jewel, pk=jewel_id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    order,created = JewelOrder.objects.get_or_create(jewel=jewel,cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, "Cart updated!")
    return redirect('cart')


@login_required(login_url='/accounts/login/')
def remove__cart(request, jewel_id):
    if request.user.is_authenticated():
        try:
            jewel = Jewel.objects.get(pk=jewel_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_cart(jewel_id)
        return redirect('cart')
    else:
        return redirect('shop')
