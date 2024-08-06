from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from userapp.serializers import UserSerializer
from rest_framework.response import Response


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        user_list = User.objects.all()
        serializer = UserSerializer(instance=user_list, many=True)
        return Response(data=serializer.data)


class UserInfo(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        user_object = User.objects.get(pk=pk)
        serializer = UserSerializer(user_object)
        return Response(serializer.data)
