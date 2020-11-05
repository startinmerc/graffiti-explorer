from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<int:pk>/', views.artist_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
