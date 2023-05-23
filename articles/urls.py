from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'),
    path('<int:article_id>/likes/', views.ArticleLikesView.as_view(), name='article_likes_view'),
    path('<int:article_id>/comments/', views.CommentsView.as_view(), name='comment_view'),
    path('<int:article_id>/comments/<int:comment_id>/', views.CommentsDetailView.as_view(), name='comments_detail_view'),
]