import factory
from faker import Faker

fake = Faker()

from factory.django import DjangoModelFactory
from users.models import UserManager, User
from articles.models import Article, Comment


"""
users 모델 팩토리
"""


class UserManagerFactory(DjangoModelFactory):
    class Meta:
        model = UserManager

    pass


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    # email = fake.email()
    # is_active = 'True'
    # is_admin = 'False'


"""
articles 모델 팩토리
"""


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = "test_article"


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
