from django.urls import reverse
from articles.serializers import ArticleSerializer
from users.models import User
from articles.models import Article, Comment
from rest_framework.test import APITestCase
from rest_framework import status


"""
article_view
article_detail_view
comment_view
comment_modify_view

"""

