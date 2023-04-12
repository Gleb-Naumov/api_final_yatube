from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.pagination import LimitOffsetPagination
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .serializers import (PostSerializer,
                          CommentSerializer,
                          GroupSerializer,
                          FollowSerializer)
from posts.models import Post, Comment, Group, Follow


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Нельзя обновлять чужой контент!')
        super(PostView, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Нельзя удалять чужой контент!')
        super(PostView, self).perform_destroy(instance)


class GroupView(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого комментария запрещено!")
        super(CommentView, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("Удаление ужого комментария запрещено!")
        super(CommentView, self).perform_destroy(instance)


class FollowView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('following__username',)
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        user = self.request.user
        return user.following.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
