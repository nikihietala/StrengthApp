import tkinter as tk
from tkinter import messagebox
from services.user_service import UsernameExistsError, user_service, LengthError


class CreateNewUserView:
    """Uuden käyttäjän luonnista vastaava näkymä."""

    def __init__(self, root, press_back_to_login):
        """Luokan konstruktori, joka luo uuden rekisteröitymisnäkymän.
        Args:
            root:
                TKinter-elementti, joka vastaa Tkinter-ikkunasta.
            press_back_to_login:
                Kutsuttava arvo, jolla siirrytään takaisin kirjautumisnäkymään.
            create_new_user:
                Kutsuttava arvo, jolla luodaan uusi käyttäjä. Saa argumentteina käyttäjänimen ja salasanan.
        """
        self._root = root
        self._frame = None
        self._press_back_to_login = press_back_to_login
        self._username_entry = None
        self._password_entry = None
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=tk.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _create_new_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user_service.create_user(username, password)
            messagebox.showinfo("Success", f"Username {username} is created!")
        except UsernameExistsError:
            messagebox.showerror("Error", f"Username {username} is taken!")
            raise UsernameExistsError("Username already exists")
        except LengthError:
            messagebox.showerror("Error", "Username or password too short!")
            raise LengthError(f'Username or password too short')

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        intro_text = tk.Label(master=self._frame, text="Create new username.")
        intro_text.pack(side=tk.TOP, anchor=tk.NW, pady=15)

        self.username_label = tk.Label(
            master=self._frame, text="Your username (at least 4 characters long)")
        self.username_label.pack()

        self.username_entry = tk.Entry(master=self._frame)
        self.username_entry.pack(fill=tk.X)

        self.password_label = tk.Label(
            master=self._frame, text="Your password (at least 6 characters long)")
        self.password_label.pack()

        self.password_entry = tk.Entry(master=self._frame)
        self.password_entry.pack(fill=tk.X)

        create_button = tk.Button(
            master=self._frame, text="CREATE NEW USER", command=self._create_new_user)
        create_button.pack(pady=10)

        back_to_login_button = tk.Button(
            master=self._frame, text="GO BACK TO LOGIN", command=self._press_back_to_login)
        back_to_login_button.pack(pady=10)
