from django.urls import path
from userapp.views import UserList


urlpatterns = [
    path("list/", UserList.as_view(), name="user-list"),

]