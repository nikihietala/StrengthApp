from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None


class UserRepository:
    """Käyttäjien tietokantaoperaatiosta vastaava luokka."""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden connection-olio.
        """
        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan kaikista User-olioista.    
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def create(self, user):
        """Tallentaa uuden käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä (user-olio)

        Returns:
            Tallennettu käyttäjä (user-olio)
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.

        Returns:
            Palauttaa käyttäjän (user-olio), jos kyseinen käyttäjätunnus löytyy tietokannasta. Muuten palauttaa None.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def clear_userlist(self):
        """Tyhjentää kaikki käyttäjät tietokannasta."""
        cursor = self._connection.cursor()
        cursor.execute('delete from users')
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()
