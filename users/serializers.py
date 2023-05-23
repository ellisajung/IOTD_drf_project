from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from articles.models import Article
from django.contrib.auth.hashers import make_password

from articles.serializers import ArticleListSerializer


class LoginViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["nickname"] = user.nickname
        token["email"] = user.email

        return token


# 특정 유저가 팔로우하고 팔로잉하는 유저 목록을 보여줌
class UserFollowSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    followings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "followers",
            "followings",
        )


class UserLikeSerializer(serializers.ModelSerializer):
    # 글 전체 목록을 불러오는 시리얼라이저(홈 피드)가 있다고 가정, 그것을 사용
    like_articles = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("like_articles",)


class UserFeedSerializer(serializers.ModelSerializer):
    # 팔로잉 하는 사용자들의 목록을 들고옴
    followings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 그 사용자들의 게시글을 찾아옴
    feeds = serializers.SerializerMethodField()

    def get_feeds(self, obj):
        feeds = Article.objects.filter(user__in=obj.followings)
        feed_serializer = ArticleListSerializer(feeds, many=True)
        return feed_serializer.data

    class Meta:
        model = User
        fields = ("feeds",)
