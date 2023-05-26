import pytest


"""
Article
Comment
"""

pytestmark = pytest.mark.django_db


class TestArticleModel:
    def test_str_method(self, article_factory):
        # Arrange
        # Act
        x = article_factory(title="test_article")
        print(x)
        # Assert
        assert x.__str__() == "test_article"


class TestCommentModel:
    def test_comment_str_method(self):
        pass
