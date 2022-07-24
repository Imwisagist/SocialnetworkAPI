from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    PostSerializer,
    CommentSerializer,
    FollowSerializer,
    GroupSerializer
)
from posts.models import Post, Group, User


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ('get', )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    http_method_names = ('get', 'post')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.user.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
        return post.comments.all()
