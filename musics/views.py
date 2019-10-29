from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Review
from rest_framework.decorators import api_view
from .serializers import MusicSerializers, ArtistSerializers, ArtistDetailSerializers, ReviewSerializers
from rest_framework.response import Response
# Create your views here.

@api_view(['GET']) # HTTP method
def music_index(request):
    '''
    음악 목록 정보
    '''
    musics = Music.objects.all()
    serializer = MusicSerializers(musics, many=True) # Query set 이라서 many=True!!
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, music_pk):
    '''
    음악 상세 정보
    '''
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializers(music)
    return Response(serializer.data)

# 아티스트 목록
@api_view(['GET'])
def artists_index(request):
    '''
    아티스트 목록
    '''
    artists = Artist.objects.all()
    serializer = ArtistSerializers(artists, many=True)
    return Response(serializer.data)

# 아티스트 상세 정보
@api_view(['GET'])
def artist_detail(request, artist_pk):
    '''
    아티스트와 해당하는 음악
    '''
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializers(artist)
    return Response(serializer.data)

# 리뷰 작성
@api_view(['POST'])
def review_create(reqeust, music_pk):
    serializer = ReviewSerializers(data=reqeust.data) # reqeust.POST form를 통해서 request.data 는 post형식으로 데이터를 보낼 때
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response({'message' : 'review가 등록 되었습니다.'})

@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializers(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message' : '성공적으로 수정 되었습니다.'})
    else:
        review.delete()
        return Response({'message' : '성공적으로 삭제 되었습니다.'})