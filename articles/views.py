from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.query_utils import Q

class ArticleView(APIView):
    """홈 : 커뮤니티 게시글 전체보기 및 작성 정보 전송 및 작성 처리 요청"""
    """글쓰기"""
    pass
class ArticleDetailView(APIView):
    """게시글 상세보기 페이지 수정 및 삭제"""
    
    pass
class ArticleLikesView(APIView):
    """게시글 좋아요 요청"""
    
    pass
class CommentsView(APIView):
    """댓글 보기 및 작성"""
    
    pass
class CommentsDetailView(APIView):
    """댓글 작성 정보 전송 및 작성 처리 요청, 수정, 삭제"""
    
    pass