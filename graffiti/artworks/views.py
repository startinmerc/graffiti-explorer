from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Artist, Artwork
from .serializers import ArtistSerializer, ArtworkSerializer

class ArtistList(APIView):
  # List all artists
  def get(self, request, format=None):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
  # Post new artist
  def post(self, request, format=None):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetail(APIView):
  # Find artist
  def get_object(self,pk):
    try:
      return Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
      raise Http404
  
  def get(self, request, pk, format=None):
    artist = self.get_object(pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    artist = self.get_object(pk)
    serializer = ArtistSerializer(artist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk, format=None):
    artist = self.get_object(pk)
    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
