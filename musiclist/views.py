from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import Album

# Create your views here.

def list_albums(request):
    albums = Album.objects.all()
    return render(request, "album/list_albums.html",
                  {"albums": albums})



# def list_albums(request):
#   list_albums = Album.objects.all()
#   return render(request, 'albums/list_albums.html', context={'musiclist':list_albums})


