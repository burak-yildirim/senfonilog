from rest_framework import viewsets
from blog.models import Tag, Blog, Comment
from .serializers import (
    TagSerializer,
    BlogListSerializer,
    BlogSerializer,
    CommentSerializer
)
from .filtersets import (
    TagFilter,
    BlogListFilter,
    BlogFilter,
    CommentFilter
)


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_class = TagFilter


class BlogListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filterset_class = BlogListFilter


class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_class = BlogFilter


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
