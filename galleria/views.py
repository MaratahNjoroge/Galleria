from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery




# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    '''
    function to display the about page and location 
    '''
    images = Gallery.filter_by_location()
    return render(request, 'about.html', {"images": images})

def gallery(request):
    gallery = Gallery.objects.all()    
    
    return render(request, 'gallery.html',{"gallery": gallery})
        
def image(request, image_id):
    images = Gallery.objects.get(id=image_id)

    return render(request, 'image.html', {"images": images})