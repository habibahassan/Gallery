from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image,Location


def homePageView(request):
    
    return render(request,'home.html')

def images(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'images.html',{"images":images, "location": location})


