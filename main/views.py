from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from main.models import Artist, Song


def show(request):
    # artist = Artist.objects.order_by("?").first()
    # print(artist)
    # albums = artist.album_set.all()
    # print(albums)
    # for alb in albums:
    #     print(alb.name, alb.release_year)
    #     songs = alb.songs.all()
    #     print(len(songs), "Songs")
    #     for s in songs:
    #         print("Song -", s.title, s.duration)
    song = Song.objects.order_by("?").first()
    print(song)
    album = song.album
    print(album)
    artists = album.artists.all().values("name")
    print(artists)

    # song.album.artists.all()

    return HttpResponse(artists)

# python manage.py runserver
