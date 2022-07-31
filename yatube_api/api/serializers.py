from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Follow, Group

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели подписок"""
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate_following(self, data):
        user = self.context['request'].user
        if user == data and self.context['request'].method == 'POST':
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        if Follow.objects.filter(
                user=user, following=data
        ).exists():
            raise serializers.ValidationError('Данная подписка уже существует')
        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow
