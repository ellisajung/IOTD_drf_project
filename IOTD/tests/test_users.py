# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IOTD.settings')

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# from users.models import User
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# import pytest
# @pytest.mark.django_db
# class LoginUserTest(APITestCase):
#     def setUp(self):

#         self.data = {'username': 'john', 'password': 'test'}
#         self.user = User.objects.create_user('john', 'test')

#     def test_login(self):
#         response = self.client.post(reverse('token_obtain_pair'), self.data)
        
#         self.assertEqual(response.status_code, 200)
        
#     def test_get_user_data(self):
#         access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
#         print(access_token)
#         response = self.client.get(
#             path=reverse("user_view"),
#             HTTP_AUTHORIZATION=f"Bearer {access_token}"
#         )
#         self.assertEqual(response.status_code, 200)

