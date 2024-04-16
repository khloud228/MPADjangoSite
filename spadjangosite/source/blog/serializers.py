from django.contrib.auth.models import User

from rest_framework import serializers

from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag

from .models import Post, Comment


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Post
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class ContactSerializer(serializers.ModelSerializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    class Meta:
        model = User
        fields = ('username', 'subject', 'message')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__   '


class RegisterSerializer(serializers.ModelSerializer):
    retry_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'retry_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        return value[0].lower() + value[1:]
    
    def validate(self, data):
        if data['password'] != data['retry_password']:
            raise serializers.ValidationError({'password':'Пароли не совпадают'})
        return data
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='slug',  queryset=Post.objects.all())
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_date')
