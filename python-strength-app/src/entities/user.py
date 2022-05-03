class User:
    """Luokka, joka kuvaa käyttäjää.

    Attributes:
        username: Käyttäjän käyttäjätunnus/käyttäjänimi (merkkijonoarvo)
        password: Käyttäjän salasana (merkkijonoarvo)
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Käyttäjän käyttäjätunnus/käyttäjänimi (merkkijonoarvo)
            password: Käyttäjän salasana (merkkijonoarvo)
        """
        self.username = username
        self.password = password
