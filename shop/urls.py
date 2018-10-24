from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^today/$',views.home,name='siteToday'),
    url('^about/',views.about,name='about'),
    url('^shop/',views.shop,name='shop'),
    url('^blog/',views.shop,name='blog'),
    url('^contact/',views.contact,name='contact'),
    url(r'^search/', views.search_results, name='search_results')
]

from django.conf import settings
from django.conf.urls.static import static