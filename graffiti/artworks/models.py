from django.db import models

# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name
    
class Artwork(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=200, default='')
  location = models.CharField(max_length=200, default='')
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  description = models.CharField(max_length=200, default='')
  photos = models.CharField(max_length=200, default='')
  def __str__(self):
    return self.title
