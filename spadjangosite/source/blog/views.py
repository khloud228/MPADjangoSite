from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    GenericAPIView
)

from django.db.models import Count
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from .models import Post, Comment
from .serializers import (
    PostSerializer, 
    TagSerializer,
    ContactSerializer,
    RegisterSerializer,
    UserSerializer,
    CommentSerializer
)
from .services import CustomPageNumberPagination

from taggit.models import Tag
from taggit_serializer.serializers import TaggitSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = (permissions.AllowAny,)
    search_fields = ('title', 'text')
    filter_backends = (SearchFilter,)



class TagDetailView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = Tag.objects.get(slug=tag_slug)
        posts = Post.objects.filter(tags=tag)
        return posts


class TagView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.AllowAny]


class AsideView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        post = Post.objects.get(slug=self.kwargs['post_slug'])
        post_tags_ids = post.tags.values_list('id', flat=True)
        related_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
        related_posts = related_posts.annotate(same_tags=Count('tags')).order_by('-same_tags')[:5]
        return related_posts


class ContactView(APIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer_class = ContactSerializer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            username = data['username']
            subject = data['subject']
            message = data['message']
            try:
                send_mail(
                    subject=f'От {username} | {subject}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    message=message,
                    recipient_list=['mrkhloud228xd@gmail.com']
                )
            except BadHeaderError:
                return Response({'error': 'Невалидный заголовок!'})
            return Response({'success': 'Sent'})


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'message': 'Пользователь успешно создан!',
            'user': UserSerializer(instance=user).data,
        })



class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response({
            'user': UserSerializer(instance=request.user).data
        })


class CommentView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        post_slug = self.kwargs['post_slug'].lower()
        post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=post)
        return comments
