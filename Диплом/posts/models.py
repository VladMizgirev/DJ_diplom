from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

like = '\u2764\uFE0F'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Post, blank=True, related_name="likes_1")
    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Post, blank=True, related_name="comments_1")
    likes = GenericRelation(Like)
    def total_likes(self):
        return self.likes.count()