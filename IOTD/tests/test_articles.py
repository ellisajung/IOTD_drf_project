import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IOTD.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from users.models import User
from articles.models import Article
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class PostingViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        response = APIClient().post(
            "/users/signup/",
            {
                "email": "test@test.com",
                "password": "test",
            },
            format="json",
        )
        return response

    def tearDown(self):
        for articles in Article.objects.all():
            articles.image.delete()
            articles.delete()

    # def test_create_posting_success(self):
    #     response = self.client.post(
    #         path=reverse("posting_view"),
    #         data=self.posting_data,
    #         HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Article.objects.count(), 1)
    #     self.assertEqual(Article.objects.get().title, "test Title")
