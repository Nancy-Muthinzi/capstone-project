from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^today/$',views.home,name='siteToday'),
    url('^profile/(\d+)', views.profile, name='profile'),
    url('^about/',views.about,name='about'),
    url(r'^collection/$',views.collection,name='collection'),
    url('^blog/',views.blog,name='blog'),
    url('^contact/',views.contact,name='contact'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^cart/', views.cart, name='cart'),  
    # url(r'^remove/(\d+)', views.remove_cart, name='remove_cart'),
    # url(r'^cart/', views.cart, name='cart'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)