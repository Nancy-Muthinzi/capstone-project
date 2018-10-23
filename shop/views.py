from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt

def home(request):
    date = dt.date.today()
    return render(request, 'home.html', {'date':date})