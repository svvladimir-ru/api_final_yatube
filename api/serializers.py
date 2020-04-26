from rest_framework import serializers
from .models import Post, Comment, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

    def validate_following(self, value):
        if Follow.objects.filter(user=self.context['request'].user, following__username=value).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого автора")
        return value


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title',)
        model = Group
