from .models  import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
''''Artiste API'''
@api_view(['GET', 'POST'])
def  get_artiste(request, format=None):
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        artiste_serializer = ArtisteSerializer(artistes, many=True)
        return Response(artiste_serializer.data)
    
    if request.method == 'POST':
        artiste_serializer = ArtisteSerializer(data=request.data)
        if artiste_serializer.is_valid():
            artiste_serializer.save()
            return Response(artiste_serializer.data, status=status.HTTP_201_CREATED)


'''ADVANCED ARTISE API'''
@api_view(['GET', 'PUT', 'DELETE'])
def  artiste_detail(request, id, format=None):
    try:
        artist = Artiste.objects.get(pk=id) 
    except  Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        artiste_serializer = ArtisteSerializer(artist)
        return Response(artiste_serializer.data)

    elif request.method == 'PUT':
            artiste_serializer = ArtisteSerializer(artist, data=request.data)
            if artiste_serializer.is_valid():
                artiste_serializer.save()
                return Response(artiste_serializer.data)
            return Response(artiste_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''''SONG API'''
@api_view(['GET', 'POST'])
def get_song(request, format=None):
    
    if request.method == 'GET':
        songs = Song.objects.all()
        song_serializer = SongSerializer(songs, many=True)
        return Response(song_serializer.data)
    
    if request.method == 'POST':
        song_serializer =   SongSerializer(data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data, status=status.HTTP_201_CREATED)

'''ADVANCED SONG API'''
@api_view(['GET', 'PUT', 'DELETE'])
def  song_detail(request, id, format=None):
    try:
        song = Song.objects.get(pk=id)
    except  Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        song_serializer = SongSerializer(song)
        return Response(song_serializer.data)

    elif request.method == 'PUT':
          song_serializer =  SongSerializer(song, data=request.data)
          if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''LYRIC API'''
@api_view(['GET', 'POST'])
def get_lyric(request, format=None):
    if request.method == 'GET':
        lyrics = Lyric.objects.all()
        lyric_serializer = LyricSerializer(lyrics, many=True)
        return Response(lyric_serializer.data)
    
    if request.method == 'POST':
        lyric_serializer = LyricSerializer(data=request.data)
        if lyric_serializer.is_valid:
            lyric_serializer.save()
            return Response(lyric_serializer.data, status=status.HTTP_201_CREATED)

'''ADVANCED LYRIC API'''
@api_view(['GET', 'PUT', 'DELETE'])
def  lyric_detail(request, id, format=None):
    try:
        lyric = Lyric.objects.id(pk=id)
    except  Lyric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        lyric_serializer = LyricSerializer(lyric)
        return Response(lyric_serializer.data)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        lyric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)