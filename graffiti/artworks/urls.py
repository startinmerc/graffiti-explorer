from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<int:pk>/', views.artist_detail),
]