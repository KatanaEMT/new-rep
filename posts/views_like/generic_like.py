from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView
from posts.models import *
from posts.serializers import LikeSerializer, DisLikeSerializer


class LikeList(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DisLikeList(ListAPIView):
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer