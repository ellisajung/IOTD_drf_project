from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView
from users import views

urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("<int:user_id>/", views.UserDeleteView.as_view(), name="user_delete_view"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("follow/<int:user_id>/", views.FollowView.as_view(), name="follow_view"),
    path("myfeed/", views.MyFeedView.as_view(), name="myfeed_view"),
    path("myfeed/like", views.MyLikeView.as_view(), name="mylike_view"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
