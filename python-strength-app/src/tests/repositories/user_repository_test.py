import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.clear_userlist()
        self.user_mies = User('mies', 'mies123')
        self.user_nainen = User('nainen', 'nainen123')

    def test_create(self):
        user_repository.create(self.user_mies)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_mies.username)

    def test_find_by_username(self):
        user_repository.create(self.user_mies)
        user = user_repository.find_by_username(self.user_mies.username)
        self.assertEqual(user.username, self.user_mies.username)

    def test_find_all(self):
        user_repository.create(self.user_mies)
        user_repository.create(self.user_nainen)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_mies.username)
        self.assertEqual(users[1].username, self.user_nainen.username)

    def test_clear_userlist(self):
        user_repository.clear_userlist()
        users = user_repository.find_all()
        self.assertEqual(len(users), 0)
