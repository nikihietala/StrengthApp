import unittest
from entities.user import User
from services.user_service import (
    UserService, LoginError, UsernameExistsError, LengthError)
from repositories.user_repository import user_repository


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.user_esimerkki = User('esimerkkieero', 'salasana123')

    def login_user(self, user):
        self.user_service.create_user(user.username, user.password)

    def test_login_with_valid_credentials(self):
        user = self.user_service.login(
            self.user_esimerkki.username, self.user_esimerkki.password)
        self.assertEqual(user.username, self.user_esimerkki.username)

    def test_login_with_invalid_credentials(self):
        self.assertRaises(LoginError, lambda: self.user_service.login(
            'invaliduser', 'invalidpassword'))

    def test_get_user(self):
        self.login_user(self.user_esimerkki)
        user = self.user_service.get_user()
        self.assertEqual(user.username, self.user_esimerkki.username)

    def test_create_user(self):
        user_repository.clear_userlist()
        self.user_service.create_user('new_user', 'password')
        users = self.user_service.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'new_user')

    def test_create_user_with_existing_username(self):
        user_repository.clear_userlist()
        self.user_service.create_user('new_user', 'password')
        users = self.user_service.get_users()
        self.assertRaises(UsernameExistsError, lambda: self.user_service.create_user(
            'new_user', 'password123'))
        self.assertEqual(len(users), 1)

    def test_create_user_with_too_short_username(self):
        user_repository.clear_userlist()
        users = self.user_service.get_users()
        self.assertRaises(
            LengthError, lambda: self.user_service.create_user('a', 'password123'))
        self.assertEqual(len(users), 0)

    def test_create_user_with_too_short_password(self):
        user_repository.clear_userlist()
        users = self.user_service.get_users()
        self.assertRaises(
            LengthError, lambda: self.user_service.create_user('valid_user', '123'))
        self.assertEqual(len(users), 0)
