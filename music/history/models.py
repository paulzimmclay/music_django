from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    song_id = models.IntegerField


class Song(models.Model):
    song_name = models.CharField(mox_length=100)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)