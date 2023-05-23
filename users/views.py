from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.query_utils import Q
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import LoginViewSerializer

class UserView(APIView):
    """회원가입 정보 전송 및 처리 요청"""
    pass

class LoginView(TokenObtainPairView):
    """로그인 정보 전송 및 처리 요청"""
    serializer_class = LoginViewSerializer

class UserDeleteView(APIView):
    """유저 정보 요청, 수정, 회원 탈퇴"""
    pass

class MypageView(APIView):
    """마이페이지 요청 및 수정"""
    pass

class FollowView(APIView):
    """팔로우/언팔로우 요청"""
    pass

class MyfeedView(APIView):
    """피드페이지(좋아요, 팔로우)"""
    pass
