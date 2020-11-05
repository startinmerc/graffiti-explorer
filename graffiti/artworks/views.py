from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Artwork
from .serializers import ArtistSerializer, ArtworkSerializer

@api_view(['GET','POST'])
def artist_list(request):
  # List all artists
  if request.method == 'GET':
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
  # Post new artist
  elif request.method == 'POST':
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def artist_detail(request, pk):
  try:
    artist = Artist.objects.get(pk=pk)
  except Artist.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = ArtistSerializer(artist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def artwork_list(request):
  if request.method == 'GET':
    artworks = Artwork.objects.all()
    serializer = ArtworkSerializer(artworks, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ArtworkSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def artwork_detail(request, pk):
  try:
    artwork = Artwork.objects.get(pk=pk)
  except Artwork.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = ArtworkSerializer(artwork)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = ArtworkSerializer(artwork, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    artwork.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)