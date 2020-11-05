from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ArtistSerializer, ArtworkSerializer
# ===FOR DEV
from django.views.decorators.csrf import csrf_exempt
# ===

from .models import Artist, Artwork

# ===FOR DEV
@csrf_exempt
# ===
def artist_list(request):
  if request.method == 'GET':
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ArtistSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

# ===FOR DEV
@csrf_exempt
# ===
def artist_detail(request, pk):
  try:
    artist = Artist.objects.get(pk=pk)
  except Artist.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ArtistSerializer(artist)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ArtistSerializer(artist, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=404)
  
  elif request.method == 'DELETE':
    artist.delete()
    return HttpResponse(status=204)

# ===FOR DEV
@csrf_exempt
# ===
def artwork_list(request):
  if request.methon == 'GET':
    artworks = Artwork.objects.all()
    serializer = ArtworkSerializer(artworks, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ArtworkSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

# ===FOR DEV
@csrf_exempt
# ===
def artwork_detail(request, pk):
  try:
    artwork = Artwork.objects.get(pk=pk)
  except Artwork.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ArtworkSerializer(artwork)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ArtworkSerializer(artwork, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=404)
  
  elif request.method == 'DELETE':
    artwork.delete()
    return HttpResponse(status=204)