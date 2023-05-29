from rest_framework import serializers
from articles.models import Article, Comment
from users.models import User

"""댓글 작성 시리얼라이저"""


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)


"""
댓글 수정 시리얼라이저
유저를 받아올 때 닉네임으로 받아오게 함
"""


class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Comment
        fields = "__all__"


"""
게시글 리스트를 불러오는 시리얼라이저
게시글 작성자의 닉네임과 프로필 이미지도 불러올 수 있게 함
"""


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


"""
게시글 작성 시리얼라이저
"""


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content", "tags")


"""
게시글 상세보기 시리얼라이저
유저를 닉네임으로 불러올 수 있게 함
"""


class ArticleDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Article
        fields = "__all__"
