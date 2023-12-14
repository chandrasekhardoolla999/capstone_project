from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError('Username is taken.')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'].lower()  # Use lower() to ensure case-insensitive uniqueness
        )
        user.set_password(validated_data['password'])
        user.save()  # Save the user object to persist changes
        return user




from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
# serializers.py


from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
# serializers.py

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
# serializers.py

from .models import Blog, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only= True)

    class Meta:
        model = Blog
        fields = '__all__'

from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
