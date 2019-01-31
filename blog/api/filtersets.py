from django_filters import rest_framework as filters
from blog.models import Tag, Blog, Comment


class TagFilter(filters.FilterSet):

    class Meta:
        model = Tag
        fields = {
            "id": ("lte", "gte", ),
            "name": ("icontains", "iexact"),
        }


class BlogListFilter(filters.FilterSet):
    tagId__iexact = filters.NumberFilter(
        field_name="tag_id", lookup_expr="exact")
    tagId__gte = filters.NumberFilter(
        field_name="tag_id", lookup_expr="gte")
    tagId__lte = filters.NumberFilter(
        field_name="tag_id", lookup_expr="lte")
    createDate__iexact = filters.DateTimeFilter(
        field_name="create_date", lookup_expr="exact")
    createDate__gte = filters.DateTimeFilter(
        field_name="create_date", lookup_expr="gte")
    createDate__lte = filters.DateTimeFilter(
        field_name="create_date", lookup_expr="lte")

    class Meta:
        model = Blog
        fields = {
            "id": ("lte", "gte"),
            "header": ("icontains", "iexact"),
            "author": ("icontains", "iexact"),
        }


class BlogFilter(BlogListFilter):
    Meta = BlogListFilter.Meta
    Meta.fields["post"] = ("icontains",)


class CommentFilter(filters.FilterSet):
    blogId__iexact = filters.NumberFilter(
        field_name="blog_id", lookup_expr="exact")
    blogId__gte = filters.NumberFilter(
        field_name="blog_id", lookup_expr="gte")
    blogId__lte = filters.NumberFilter(
        field_name="blog_id", lookup_expr="lte")
    createDate__iexact = filters.DateTimeFilter(
        field_name="create_date", lookup_expr="exact")
    createDate__gte = filters.DateTimeFilter(
        field_name="create_date", lookup_expr="gte")
    createDate__lte = filters.DateTimeFilter(
        field_name="create_date", lookup_expr="lte")
    authorEmail__iexact = filters.CharFilter(
        field_name="author_email", lookup_expr="exact")
    authorEmail__icontains = filters.CharFilter(
        field_name="author_email", lookup_expr="contains")

    class Meta:
        model = Comment
        fields = {
            "id": ("lte", "gte"),
            "text": ("icontains", "iexact"),
            "author": ("icontains", "iexact"),
        }
