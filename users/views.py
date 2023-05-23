from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.query_utils import Q
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from users.serializers import UserLikeSerializer, UserFollowSerializer, UserFeedSerializer, LoginViewSerializer


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
    # 특정 유저의 이름, 아이디, 팔로우/팔로잉 목록 반환
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserFollowSerializer(user)
        return Response(serializer.data)

    # 특정 유저를 팔로우하기
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("팔로우 취소", status=status.HTTP_204_NO_CONTENT)
        else:
            you.followers.add(me)
            return Response("팔로우", status=status.HTTP_200_OK)


# 내가 팔로우 한 사용자의 게시글을 받아옴
class MyFeedView(APIView):
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserFeedSerializer(user)
        return Response(serializer.data)


# 내가 좋아요 한 게시글을 받아옴
class MyLikeView(APIView):
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserLikeSerializer(user)
        return Response(serializer.data)
