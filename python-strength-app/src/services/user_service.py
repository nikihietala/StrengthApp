from entities.user import User
from repositories.user_repository import (user_repository as user_rep)


class UsernameExistsError(Exception):
    pass


class LoginError(Exception):
    pass


class LengthError(Exception):
    pass


class UserService:
    """Käyttäjän sovelluslogiikasta vastaava luokka"""

    def __init__(self, user_repository=user_rep):
        """Luokan konstruktori. Luo uuden palvelun käyttäjän sovelluslogiikkaa varten.

            Args:
                user_repository: Olio, jolla on User-Repository luokan metodit.
        """
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän.

        Args:
            username: käyttäjän luoma käyttäjätunnus
            password: käyttäjän luoma salasana
            login:
                Oletusarvo True.
                Boolean-arvo, joka kertoo onnistuuko kirjautuminen.
        Raises:
            LengthError:
                Virhe, joka tapahtuu jos käyttäjätunnus tai salasana ovat liian lyhyitä.
            UsernameExistsError:
                Virhe, joka tapahtuu jos käyttäjän valitsema käyttäjätunnus on jo käytössä.
        Returns:
            Luotu käyttäjä (User-olio).
        """
        user_exists = self._user_repository.find_by_username(username)
        if len(username) < 4 or len(password) < 6:
            raise LengthError('Username or password too short')
        if user_exists:
            raise UsernameExistsError(f'Username {username} already exists!')

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: käyttäjän luoma käyttäjätunnus
            password: käyttäjän luoma salasana
        Raises:
            LoginError: Virhe, joka tapahtuu jos käyttäjätunnus tai salasana on väärin.
        Returns:
            Kirjautunut käyttäjä (User-olio).
        """
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise LoginError('Wrong username or password, try again.')

        self._user = user
        return user

    def get_user(self):
        """Palauttaa nykyisen käyttäjän.

        Returns:
            Kirjautunut käyttäjä (User-olio).
        """
        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Listan kaikista käyttäjistä (User-olioita).
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self._user = None


user_service = UserService()
