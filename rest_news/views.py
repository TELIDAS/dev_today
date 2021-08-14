from django.contrib.auth.models import User
from rest_framework import generics

from news_board.models import Post, Comment
from rest_news.serializers import PostSerializer, RegisterSerializer, LoginSerializer, CommentSerializer


class PostGenericAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostGenericDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'id'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    lookup_field = 'id'


class CommentGenericAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentGenericDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
