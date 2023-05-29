from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.query_utils import Q
from articles.models import Article, Comment
from articles.serializers import (
    ArticleCreateSerializer,
    ArticleListSerializer,
    ArticleDetailSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer,
)


class ArticleView(APIView):
    """홈 : 커뮤니티 게시글 전체보기"""

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """게시글 작성"""

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "게시글 작성완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    """게시글 상세 페이지 보기"""

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleDetailSerializer(article)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """게시글 수정"""

    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            serializer = ArticleDetailSerializer(
                article, data=request.data, partial=True
            )

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("수정 권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    """게시글 삭제"""

    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response("삭제 완료", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("수정 권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)


class ArticleLikesView(APIView):
    """게시글 좋아요 요청"""

    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user not in article.likes.all():
            article.likes.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)
        else:
            article.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_205_RESET_CONTENT)


class CommentsView(APIView):
    """댓글 작성"""

    def post(self, request, article_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user, article=Article.objects.get(pk=article_id)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class CommentsDetailView(APIView):
    """댓글 수정"""

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            serializer = CommentDetailSerializer(
                comment, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("수정 권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    """댓글 삭제"""

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response("삭제 완료", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("수정 권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
