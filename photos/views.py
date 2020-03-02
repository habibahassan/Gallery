from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image,Location


def homePage(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'home.html',{"images":images, "location": location})

def searchbycategory(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        print(search_term)
        found_images = Image.search_by_category(search_term)
        print(found_images)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"images":found_images})
    else:
        message="No searched category"
        return render(request,'search.html',{"message":message})
    
def searchbylocation(request, location):
    locations = Location.objects.all()
    images = Image.search_by_location(location)
    print(images)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title': title, 'images': images, 'locations': locations})
