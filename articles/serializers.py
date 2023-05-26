from rest_framework import serializers
from articles.models import Article, Comment
from users.models import User


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    profile_img = serializers.SerializerMethodField()

    def get_nickname(self, obj):
        user = User.objects.get(id=obj.user.id)
        return user.nickname
    
    def get_profile_img(self, obj):
        user = User.objects.get(id=obj.user.id)
        return user.profile_img.url if user.profile_img else None
    
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content", "tags")


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
