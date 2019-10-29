from django.shortcuts import render, get_object_or_404
from .models import Music
from rest_framework.decorators import api_view
from .serializers import MusicSerializers
from rest_framework.response import Response
# Create your views here.

@api_view(['GET']) # HTTP method
def index(request):
    musics = Music.objects.all()
    serializer = MusicSerializers(musics, many=True) # Query set 이라서 many=True!!
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializers(music)
    return Response(serializer.data)