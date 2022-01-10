from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated
)

from posts.models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)
from .mixins import CreateListViewSet

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Viewset для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Переопределяем сохранение автора."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewset(viewsets.ModelViewSet):
    """Viewset для модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Получаем queryset комментов к посту с нужным id."""
        post = get_object_or_404(Post, id=self.kwargs["id"])
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        """Переопределяем сохранение автора и id поста."""
        post = get_object_or_404(Post, id=self.kwargs["id"])
        serializer.save(author=self.request.user, post=post)


class FollowViewset(CreateListViewSet):
    """Viewset для модели Follow."""
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        """Получаем queryset авторов, на кого подписан user."""
        user = self.request.user
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
