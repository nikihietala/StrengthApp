from entities.user import User
from repositories.user_repository import (user_repository as user_rep)

class UsernameExistsError(Exception):
    pass

class LoginError(Exception):
    pass

class UserService:
    def __init__(self, user_repository=user_rep):
        self._user = None
        self._user_repository = user_repository


    def create_user(self, username, password, login=True):
        user_exists = self._user_repository.find_by_username(username)
        if user_exists:
            raise UsernameExistsError(f'Username {username} already exists!')

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user
    
    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise LoginError('Wrong username or password, try again.')

        self._user = user
        return user
    
    def get_users(self):
        return self._user_repository.find_all()

    def logout(self):
        self._user = None

user_service = UserService()

        

