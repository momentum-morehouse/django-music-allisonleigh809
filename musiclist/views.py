from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import Album

# Create your views here.

def list_album(request):
  list_album = Album.objects.all()
  return render(request, 'albums/list_album.html', context={'musiclist':list_album})
