from django.db import models

# Create your models here.

class Album:
  artistname = models.CharField(max_length=225)
  albumtitle = models.CharField(max_length=225)
  released = models.DateField()

  def __str__(self):
      return f"{self.albumtitle}"

