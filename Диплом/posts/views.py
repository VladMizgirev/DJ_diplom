from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permitions import IsOvnerOrReadOnly

from posts.models import Post, Like

from posts.serializers import PostSerializer, LikeSerializer, CommentSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOvnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        return super().perform_create(serializer)
    
class LikeViewSet(ModelViewSet):
    pass 

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

