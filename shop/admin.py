from django.contrib import admin
from .models import Product, Profile, Blog, Category

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Category)



