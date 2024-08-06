from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentInfo(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer