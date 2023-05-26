import factory
from articles.models import Article, Comment


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    # user = factory.SubFactory(UserFactory)
    title = "test_article"
    # content = "test_content"
    # image =
    # likes = factory.SubFactory(UserFactory)
    # tags = "test_tags"

    # created_at =
    # updated_at =


# class ArticleFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Article

#     title = "test_article"
