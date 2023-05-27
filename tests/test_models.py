import pytest

pytestmark = pytest.mark.django_db


"""
users 모델 테스트
"""


# UserManager
class TestUserManagerModel:
    def test_str_method(self, user_manager_factory):
        # Arrange
        # Act
        obj = user_manager_factory()
        # Assert
        assert obj.__str__() == "test_user_manager"


# User
class TestUserModel:
    def test_str_method(self, user_factory):
        # Arrange
        # Act
        obj = user_factory()
        # Assert
        assert obj.__str__() == "test_user"


"""
articles 모델 테스트
"""


# Article
class TestArticleModel:
    def test_str_method(self, article_factory):
        # Arrange
        # Act
        obj = article_factory()
        # Assert
        assert obj.__str__() == "test_article"


# Comment
class TestCommentModel:
    def test_str_method(self, comment_factory):
        # Arrange
        # Act
        obj = comment_factory()
        # Assert
        assert obj.__str__() == "test_comment"
