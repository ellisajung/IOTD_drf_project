from rest_framework import serializers
from .models import User
from articles.models import Article

from articles.serializers import ArticleListSerializer


# 특정 유저가 팔로우하고 팔로잉하는 유저 목록을 보여줌
class UserFollowSerializer(serializers.Serializer):
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


class UserLikeSerializer(serializers.Serializer):
    # 글 전체 목록을 불러오는 시리얼라이저(홈 피드)가 있다고 가정, 그것을 사용
    like_articles = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("like_articles",)


class UserFeedSerializer(serializers.Serializer):
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
