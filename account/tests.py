from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .views import *


User = get_user_model()


class AuthTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='user@gmail.com',
            password='12345678',
            is_active=True,
            activation_code='567test'
        )

    
    def test_register(self):
        data = {
            'email': 'test@gmail.com',
            'password': '123456',
            'name': 'test',
            'password_confirm': '123456'
        }

        request = self.factory.post('api/v1/register/', data, format='json')
        # print(request)
        view = RegistrationView.as_view()
        response = view(request)
        # print(response.data)

        # assert response.status_code == 201
        assert User.objects.filter(email=data['email']).exists()


    def test_login(self):
        data = {
            'email': 'user@gmail.com',
            'password': '12345678'
        }
        request = self.factory.post('/login/', data, format='json')
        view = LoginView.as_view()
        response = view(request)

        assert 'token' in response.data


    def test_change_password(self):
        data = {
            'old_password': '12345678',
            'new_password': '123456test',
            'new_password_confirm': '123456test'
        }

        request = self.factory.patch('change-password/', data)
        force_authenticate(request, self.user)
        view = ChangePasswordView.as_view()
        response = view(request)
        # print(response.data) 
        # print(User.objects.get(email=self.user.email).password)
        # print(make_password(data['new_password']))
        # assert make_password(data['new_password']) == User.objects.get(email=self.user.email).password

        assert response.status_code == 200

    def test_forgot_password(self):
        data = {
            'email': 'user@gmail.com'
        }
        request = self.factory.post('forgot-password/', data)
        view = ForgotPasswordView.as_view()
        response = view(request)
        # print(response.data)

        # assert response.status_code == 200
        self.assertEqual(response.status_code, 200)