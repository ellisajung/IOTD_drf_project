from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users import views

urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("profile/", views.UserProfileView.as_view(), name="user_edit_view"),
    path(
        "profile/<int:user_id>/", views.UserProfileView.as_view(), name="user_edit_view"
    ),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("follow/<int:user_id>/", views.FollowView.as_view(), name="follow_view"),
    path("myfeed/", views.MyFeedView.as_view(), name="myfeed_view"),
    path("myfeed/like/", views.MyLikeView.as_view(), name="mylike_view"),
    path(
        "verify/<str:uidb64>/<str:token>/",
        views.EmailVerifyView.as_view(),
        name="email_verify_view",
    ),
]
