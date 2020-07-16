from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import Album
from .forms import albumsForm
# Create your views here.

def list_albums(request):
    albums = Album.objects.all()
    return render(request, "album/list_albums.html",
                  {"albums": albums})

def add_album(request):
    if request.method == 'GET':
        form = albumsForm()
    else:
        form = albumsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})  

def delete_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_albums.html",
                  {"album": album})

def edit_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = albumsForm(instance=album)
    else:
        form = albumsForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_albums.html", {
        "form": form,
        "album": album
    })
