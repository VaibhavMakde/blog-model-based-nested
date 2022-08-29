from rest_framework import serializers
from blog.models import Post, Author


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class AutherSerializer(serializers.ModelSerializer):
    blog_posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email', 'blog_posts']
