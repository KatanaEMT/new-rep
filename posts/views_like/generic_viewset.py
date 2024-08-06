from rest_framework import viewsets
from posts.models import Like, DisLike
from posts.serializers import LikeSerializer, DisLikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DisLikeViewSet(viewsets.ModelViewSet):
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer