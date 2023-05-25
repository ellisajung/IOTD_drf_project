from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.query_utils import Q
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from users.serializers import (
    UserSerializer,
    UserProfileSerializer,
    UserUpdateSerializer,
    UserLikeSerializer,
    UserFollowSerializer,
    UserFeedSerializer,
    LoginViewSerializer,
)


class UserView(APIView):
    # 회원가입 정보 전송 및 처리 요청
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(TokenObtainPairView):
    """로그인 정보 전송 및 처리 요청"""
    serializer_class = LoginViewSerializer


class UserDeleteView(APIView):
    # 유저 정보 요청, 수정, 회원 탈퇴

    """
    유저 정보 요청
    user_id로 아무나 프로필 조회 가능
    """
    # user/profile/<int:user_id>/
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        return Response(UserProfileSerializer(user).data, status=status.HTTP_200_OK)

    """
    유저 정보 수정
    """
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    회원 탈퇴
    is_active = False로 변경만 하고 회원 정보는 계속 보관
    email(아이디), name 남아있어서 탈퇴한 회원이 같은 정보로 재가입 불가
    """

    def delete(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response({"message": "회원 탈퇴!"})


# class MypageView(APIView):
#     """마이페이지 요청"""

#     pass


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
        if me != you:
            if me in you.followers.all():
                you.followers.remove(me)
                return Response("팔로우 취소", status=status.HTTP_204_NO_CONTENT)
            else:
                you.followers.add(me)
                return Response("팔로우", status=status.HTTP_200_OK)
        else:
            return Response("자신은 팔로우 할 수 없습니다.")


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
