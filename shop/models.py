from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    names = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.names

    class Meta:
        ordering = ['names']


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='home/', blank=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=75)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.get(pk=id)
        return images

class Category(models.Model):
    name = models.CharField(max_length =25)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

    def __str__(self):
        return self.name

class Blog(models.Model):
    date = models.DateField()
    image = models.ImageField(upload_to='blog/', blank=True)
    title = models.CharField(max_length=100)
    post = models.TextField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def __unicode__(self): 
            return "%s" % (self.user)

    def add_to_cart(self, jewel_id):
        jewel = Jewel.objects.get(pk=jewel_id)
        try:
            preexisting_order = JewelOrder.objects.get(jewel=jewel, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except JewelOrder.DoesNotExist:
            new_order = JewelOrder.objects.create(
                jewel=jewel,
                cart=self,
                quantity=1
                )
            new_order.save()


    def remove_from_cart(self, jewel_id):
        jewel = Jewel.objects.get(pk=jewel_id)
        try:
            preexisting_order = JewelOrder.objects.get(jewel=jewel, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except JewelOrder.DoesNotExist:
            pass   

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()