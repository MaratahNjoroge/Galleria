from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery




# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request): 
   
    return render(request, 'galleria.html')

def gallery(request):
    gallery = Gallery.objects.all()      
    return render(request, 'gallery.html',{"gallery": gallery})
        
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Gallery.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request, image_id):
   
    image = Gallery.objects.get(id=image_id)
     
    return render(request, 'image.html', {"gallery": image})