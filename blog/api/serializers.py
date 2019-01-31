from rest_framework import serializers
from blog.models import Tag, Blog, Comment


class ForeingKeyIdField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(pk=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ("id", "name")


class BlogListSerializer(serializers.HyperlinkedModelSerializer):
    tagId = ForeingKeyIdField(source="tag", queryset=Tag.objects.all())
    createDate = serializers.DateTimeField(source="create_date")

    class Meta:
        model = Blog
        fields = ("id", "header", "author", "tagId", "createDate")


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    tagId = ForeingKeyIdField(source="tag", queryset=Tag.objects.all())
    createDate = serializers.DateTimeField(
        source="create_date", read_only=True)

    class Meta:
        model = Blog
        fields = ("id", "header", "post", "author", "tagId", "createDate")


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    blogId = ForeingKeyIdField(source="blog", queryset=Blog.objects.all())
    authorEmail = serializers.EmailField(source="author_email")
    createDate = serializers.DateTimeField(
        source="create_date", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "text", "author",
                  "authorEmail", "blogId", "createDate")
