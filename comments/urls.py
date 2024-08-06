from django.urls import path, include
from comments.views.generic_one import *
from comments.views.generic_two import *
from rest_framework import routers
from comments.views.generic_viewset import *

comment_router = routers.DefaultRouter()
comment_router.register("viewset", CommentViewSet)

urlpatterns = [
    path('v1/list/', CommentList.as_view()),
    path('v1/create/', CommentCreateAPIView.as_view()),
    path('v1/detail/<int:pk>/', CommentDetailAPIView.as_view()),
    path('v1/update/<int:pk>/', CommentUpdateAPIView.as_view()),
    path('v1/delete/<int:pk>/', CommentDeleteAPIView.as_view()),

    path('v2/list-create/', CommentListCreate.as_view()),
    path('v2/info/<int:pk>/', CommentInfo.as_view()),

    path('v3/', include(comment_router.urls))
]