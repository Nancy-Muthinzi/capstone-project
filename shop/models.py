from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
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

# class OrderItem(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now=True)
#     date_ordered = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.item.name

# class Order(models.Model):
#     ref_code = models.CharField(max_length=25)
#     owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.ManyToManyField(OrderItem)
#     items = models.ManyToManyField(OrderItem)
#     date_ordered = models.DateTimeField(auto_now=True)  
#     # payment_details = models.ForeignKey(Payment, null=True)      

#     def get_cart_items(self):
#         return self.items.all()

#     def get_cart_total(self):
#         return sum([item.product.price for item in self.items.all()])

#     def __str__(self):
#         return '{0} - {1}'.format(self.owner, self.ref_code)    

# class Cart(models.Model):
#     user = models.ForeignKey(User)
#     active = models.BooleanField(default=True)
#     order_date = models.DateField(null=True)
#     payment_type = models.CharField(max_length=100, null=True)
#     payment_id = models.CharField(max_length=100, null=True)

#     def __unicode__(self):
#         return "%s" % (self.user)

#     def add_to_cart(self, jewel_id):
#         jewel = Jewel.objects.get(pk=jewel_id)
#         try:
#             preexisting_order = JewelOrder.objects.get(jewel=jewel, cart=self)
#             preexisting_order.quantity += 1
#             preexisting_order.save()
#         except JewelOrder.DoesNotExist:
#             new_order = JewelOrder.objects.create(
#                 jewel=jewel,
#                 cart=self,
#                 quantity=1
#             )
#             new_order.save()

#     def remove_from_cart(self, jewel_id):
#         jewel = Jewel.objects.get(pk=jewel_id)
#         try:
#             preexisting_order = JewelOrder.objects.get(jewel=jewel, cart=self)
#             if preexisting_order.quantity > 1:
#                 preexisting_order.quantity -= 1
#                 preexisting_order.save()
#             else:
#                 preexisting_order.delete()
#         except JewelOrder.DoesNotExist:
#             pass


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
