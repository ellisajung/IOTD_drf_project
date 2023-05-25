# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IOTD.settings")

# from django.core.wsgi import get_wsgi_application

# application = get_wsgi_application()

# from users.models import User
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# import pytest
# from rest_framework.test import APIClient


# @pytest.mark.django_db
# def test_sign_up():
# response = APIClient().post(
#     "/users/signup/",
#     {
#         "email": "test@test.com",
#         "password": "test",
#     },
#     format="json",
# )
#     assert response.status_code == 201
