from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Product, Blog, Profile
from .forms import NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()

    return render(request, 'home.html', {'date': date})

# @login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    return render(request, 'profile.html', {'profile': profile})

def about(request):
    return render(request, 'about.html')

# @login_required(login_url='/accounts/login/')
def collection(request):
    products = Product.objects.all()

    return render(request, 'collection.html', {'products':products})

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    blog = Blog.objects.all()
    
    return render(request, 'blog.html', {'blog':blog})

def search_results(request):

    if 'item' in request.GET and request.GET["item"]:
        search_term = request.GET.get("item")
        searched_items = Item.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "items": searched_items})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message": message})

# def my_profile(request):
#     my_user_profile = Profile.objects.filter(user=request.user).first()
#     my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
#     context = {
#         'my_orders': my_orders
#     }

#     return render(request, 'profile.html', context)

# def product_list(request):
#     object_list = Product.objects.all()
#     filtered_orders = Order.objects.filter(owner=request.user.profile)
#     current_order_products = []
#     if filtered_orders.exists():
#         user_order = filtered_orders[0]
#         user_order_items = user_order.items.all()
#         current_order_products = [product.product for product in user_order_items]

#         context = {
#             'object_list': object_list,
#             'current_order_products' : current_order_products
#         }

#     return render(request, 'product_list.html', context)

@login_required(login_url='/accounts/login/')
def add_cart(request,**kwargs):
    jewel = get_object_or_404(Jewel, pk=jewel_id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    order,created = JewelOrder.objects.get_or_create(jewel=jewel,cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, "Cart updated!")
    return redirect('cart')


@login_required(login_url='/accounts/login/')
def remove_cart(request, jewel_id):
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
        return redirect('collection')
