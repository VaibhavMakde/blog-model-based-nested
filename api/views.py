from rest_framework import viewsets
from api.serializers import PostSerializer, AutherSerializer
from blog.models import Post, Author
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class AutherModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AutherSerializer
