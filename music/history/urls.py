from django.urls import path

from . import views

urlpatterns = [
    path('artist_list', views.artist_list, name='artist_list'),
    path('artist_details', views.artist_details, name='artist_details'),
]