from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from main.models import Ads, Comment
from .serializers import AdsSerializer, AdsDetailSerializer, CommentSerializer


# all ads
@api_view(['GET'])
def ads(request):
    if request.method == 'GET':
        ads = Ads.objects.filter(is_active=True)[:10]
        serializer = AdsSerializer(ads, many=True)
        return Response(serializer.data)


# ad detail
class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.filter(is_active=True)
    serializer_class = AdsDetailSerializer


# comments
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comments(request, pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        comments = Comment.objects.filter(is_active=True, ads=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
