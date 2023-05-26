from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from articles.models import Article
from django.contrib.auth.hashers import make_password

from articles.serializers import ArticleListSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_followings_count(self, obj):
        return obj.followings.count()

    class Meta:
        model = User
        fields = ("id", "email", "nickname", "profile_img", "fashion", "followings")


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password", "nickname", "profile_img", "fashion")
        read_only_fields = [
            "email",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
            "nickname": {
                "required": False,
            },
        }

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


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
    followers = UserProfileSerializer(many=True, read_only=True)
    followings = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "nickname",
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
