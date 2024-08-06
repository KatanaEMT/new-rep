from django.urls import path
from posts.views import *
from django.urls import path, include
from posts.views_like.generic_like import *
from posts.views_like.generic_viewset import *
from rest_framework import routers

like_dislike_router = routers.DefaultRouter()
like_dislike_router.register("likes", LikeViewSet)
like_dislike_router = routers.DefaultRouter()
like_dislike_router.register("Dislikes", DisLikeViewSet)


urlpatterns = [
    path("list/", PostsList.as_view(), name="posts-list"),
    path('info/<int:pk>/', PostInfo.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),

    path('v1/likelist/', LikeList.as_view()),
    path('v1/dislikelist/', DisLikeList.as_view()),
    path('v3/', include(like_dislike_router.urls))

]

