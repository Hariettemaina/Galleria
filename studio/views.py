from django.shortcuts import render
from . models import *

# Create your views here.
def homepage(request):
    images = Images.objects.all()
    return render(request,'studio/homepage.html',{'images':images})


def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'studio/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'studio/search.html',{"message":message})

