from rest_framework import serializers

from posts.models import Post, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'created_at', 'text']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['likes']

class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['user', 'img', 'created_at', 'text', 'total_likes', 'comments']
        read_only_fields = ['user',]
