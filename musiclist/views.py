from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import Album

# Create your views here.

def list_album(request):
    micpro = Album.objects.all()
    return render(request, "album/list_album.html",
                  {"micpro": micpro}) 