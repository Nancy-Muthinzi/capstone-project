from django.contrib import admin
from .models import Image, Profile, Blog, Category, Cart

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Image, ImageAdmin)
admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Cart)

