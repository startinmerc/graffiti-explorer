from django.db import models

# Create your models here.

class Artist(models.Model):
  # String
  name = models.CharField(max_length=200, default='Artist Name')
  def __str__(self):
    return self.name
    
# PY Model
class Artwork(models.Model):
  # Auto stuff
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)
  # Artwork title
  title = models.CharField(max_length=200, default='Artwork Title')
  # Artwork description
  description = models.CharField(max_length=280, default='')
  # Key of artist linked
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  # Coordinates
  coord_lat = models.FloatField()
  coord_long = models.FloatField()
  # Comma seperated urls
  photos = models.TextField(default='')
  def __str__(self):
    return self.title
