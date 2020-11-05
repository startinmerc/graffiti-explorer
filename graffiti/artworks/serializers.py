from rest_framework import serializers
from .models import Artist, Artwork

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ['name']

class ArtworkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artwork
    fields = ['title', 'location', 'artist', 'description', 'photos']
