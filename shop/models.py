from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
   instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    names = models.CharField(max_length=50)
    email = models.EmailField()
    product = models.ManyToManyField('Product', blank=True)


class Category(models.Model):
    name = models.CharField(max_length=25)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='shop/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

    @classmethod
    def retrive_all_products(cls):
        products = Product.objects.all()
        return products

    @classmethod
    def get_product_by_id(cls, id):
        products = cls.objects.get(pk=id)
        return products


class Blog(models.Model):
    date = models.DateField()
    image = models.ImageField(upload_to='blog/', blank=True)
    title = models.CharField(max_length=100)
    post = models.TextField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)

    subtotal = models.DecimalField(
        default=0.00, max_digits=12, decimal_places=2)

    total = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # objects = CartManager()

    def __str__(self):
        return str(self.id)


# class CartManager(models.Manager):
#     def get_or_new(self, request):
#         cart_id = request.session.get('cart_id', None)
#         qs = self.get_queryset().filter(id=cart_id)
#         if qs.count() == 1:
#             new_obj = False
#             cart_obj = qs.first()
#             if request.user.is_authenticated() and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#         else:
#             new_obj = True
#             cart_obj = Cart.objects.new_cart(user = request.user)
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
