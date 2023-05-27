from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import random, string

from .models import User
from .tokens import user_verify_token
from articles.models import Article
from articles.serializers import ArticleListSerializer


# 랜덤 영문숫자 6글자의 비밀번호를 return하는 함수
def reset_password():
    new_str = string.ascii_letters + string.digits
    return "".join(random.choice(new_str) for _ in range(6))


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

        # url에 포함될 user.id 에러 방지용  encoding하기
        uidb64 = urlsafe_base64_encode(force_bytes(user.id))
        # tokens.py에서 함수 호출
        token = user_verify_token.make_token(user)
        to_email = user.email
        email = EmailMessage(
            f"IOTD : {user.nickname}님의 이메일 인증",
            f"아래의 링크를 눌러 이메일 인증을 완료해주세요.\n\nhttp://127.0.0.1:8000/users/verify/{uidb64}/{token}",
            to=[to_email],
        )
        email.send()
        return user


class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

    def update(self, instance, validated_data):
        password = reset_password()
        instance.set_password(password)
        instance.save()

        to_email = instance.email
        email = EmailMessage(
            "IOTD : 비밀번호 변경 이메일",
            f"변경된 임시 비밀번호는 {password} 입니다. \n\n 로그인 후 반드시 회원 정보 수정에서 비밀번호를 변경해주세요.",
            to=[to_email],
        )
        email.send()

        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, obj):
        articles = obj.my_articles.all()  # user와 관련된 Article 객체들을 가져옴
        article_serializer = ArticleListSerializer(articles, many=True)
        return article_serializer.data

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_followings_count(self, obj):
        return obj.followings.count()

    articles = serializers.SerializerMethodField()

    def get_articles(self, obj):
        articles = Article.objects.filter(pk=obj.id)
        serializer = ArticleListSerializer(articles, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "nickname",
            "profile_img",
            "fashion",
            "followers",
            "followings",
            "articles",
        )


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
    feeds = serializers.SerializerMethodField()

    def get_feeds(self, obj):
        followings = obj.followings.all()  # ManyRelatedManager 객체를 실제 객체 목록으로 변환
        feeds = Article.objects.filter(user__in=followings)
        feed_serializer = ArticleListSerializer(feeds, many=True)
        return feed_serializer.data

    class Meta:
        model = User
        fields = ("feeds",)
