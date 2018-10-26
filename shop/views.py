from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Product, Blog, Profile, Cart
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

    if 'product' in request.GET and request.GET["product"]:
        search_term = request.GET.get("product")
        searched_items = Item.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "products": searched_items})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message": message})

def index(request):
    response = render_to_response('buylist/Home.html')
    visits = int(request.COOKIES.get('visits', '0'))
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).days > 0:
            response.set_cookie('visits', visits + 1)
            response.set_cookie('last_visit', datetime.now())
    else:
        response.set_cookie('last_visit', datetime.now())
    return response

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = Product.objects.get(id=product_id)
    cart[product_id] = product
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse("cart"))

def cart_update(request):
    p = request.POST.get("product_id")
    if p is not None:
        product_obj = Product.objects.get(id =p)
        c,n = Cart.objects.get_or_new(request)
        if product_obj not in c.products.all():
            c.products.add(product_obj)

    else:
        c.products.remove(product_obj)
        print("to be added")

    return redirect("cart:home")

def get_cart(request):
    cart = request.session.get('cart',{})
    return render(request, 'buylist/cart.html', cart)

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

# @login_required(login_url='/accounts/login/')
# def add_cart(request,**kwargs):
#     jewel = get_object_or_404(Jewel, pk=jewel_id)
#     cart,created = Cart.objects.get_or_create(user=request.user, active=True)
#     order,created = JewelOrder.objects.get_or_create(jewel=jewel,cart=cart)
#     order.quantity += 1
#     order.save()
#     messages.success(request, "Cart updated!")
#     return redirect('cart')


# @login_required(login_url='/accounts/login/')
# def remove_cart(request, jewel_id):
#     if request.user.is_authenticated():
#         try:
#             jewel = Jewel.objects.get(pk=jewel_id)
#         except ObjectDoesNotExist:
#             pass
#         else:
#             cart = Cart.objects.get(user=request.user, active=True)
#             cart.remove_cart(jewel_id)
#         return redirect('cart')
#     else:
#         return redirect('collection')
