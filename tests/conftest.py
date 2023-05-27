import pytest

from pytest_factoryboy import register
from factories import UserManagerFactory, UserFactory, ArticleFactory, CommentFactory


"""
users 모델 팩토리
"""
register(UserManagerFactory)
register(UserFactory)


# @pytest.fixture
# def new_user(db, user_factory):
#     user = user_factory.create()
#     return user


"""
articles 모델 팩토리
"""
register(ArticleFactory)
register(CommentFactory)
