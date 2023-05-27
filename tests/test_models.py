# import pytest
# from users.models import UserManager, User
# from articles.models import Article, Comment

# pytestmark = pytest.mark.django_db


# """
# users 모델 테스트
# """


# # UserManager
# @pytest.mark.django_db
# class TestUserManagerModel:
#     def test_str_method(self, user_manager_factory):
#         # Arrange
#         # Act
#         obj = user_manager_factory()
#         # Assert
#         assert obj.__str__() == "test_user_manager"


# # User
# @pytest.mark.django_db
# class TestUserModel:
#     def test_new_user(new_user):
#         print(new_user.email)
#         assert True

#     def test_str_method(self, user_factory):
#         # Arrange
#         # Act
#         obj = user_factory()
#         # Assert
#         assert obj.__str__() == "test_user"


# """
# articles 모델 테스트
# """


# # Article
# @pytest.mark.django_db
# class TestArticleModel:
#     def test_str_method(self, article_factory):
#         # Arrange
#         # Act
#         obj = article_factory()
#         # Assert
#         assert obj.__str__() == "test_article"


# # Comment
# @pytest.mark.django_db
# class TestCommentModel:
#     def test_str_method(self, comment_factory):
#         # Arrange
#         # Act
#         obj = comment_factory()
#         # Assert
#         assert obj.__str__() == "test_comment"
