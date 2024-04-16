from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet, 
    TagDetailView, 
    TagView, 
    AsideView,
    ContactView,
    RegisterView,
    ProfileView,
    CommentView
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path('posts/<slug:post_slug>/comments/', CommentView.as_view()),
    path('posts/<slug:post_slug>/aside/', AsideView.as_view()),
    path('posts/tags/<slug:tag_slug>/', TagDetailView.as_view()),
    path('posts/tags/', TagView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view())
]
