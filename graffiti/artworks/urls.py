from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>/', views.ArtistDetail.as_view()),
    path('artworks/', views.ArtworkList.as_view()),
    path('artworks/<int:pk>/', views.ArtworkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
