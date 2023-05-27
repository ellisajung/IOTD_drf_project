from pytest_factoryboy import register
from factories import UserManagerFactory, UserFactory, ArticleFactory, CommentFactory


"""
users 모델 팩토리
"""
register(UserManagerFactory)
register(UserFactory)


"""
articles 모델 팩토리
"""
register(ArticleFactory)
register(CommentFactory)
