import tkinter as tk
from services.user_service import user_service, LoginError
from tkinter import messagebox

class LoginView:
    def __init__(self, root, press_create_new_user, press_login):
        self._root = root
        self._frame = None
        self._press_create_new_user = press_create_new_user
        self._press_login = press_login
        self._initialize()

    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()

    def _check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user_service.login(username, password)
            self._press_login()
        except LoginError:
            messagebox.showerror("Error", f"Wrong username or password")
            raise LoginError("Wrong username or password, try again.")      


    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        intro_text = tk.Label(master=self._frame,
                              text="Welcome to StrengthApp. Please login.")
        intro_text.pack(side=tk.TOP, anchor=tk.NW, pady=15)

        username_label = tk.Label(master=self._frame, text="Username")
        username_label.pack()

        self.username_entry = tk.Entry(master=self._frame)
        self.username_entry.pack(fill=tk.X)

        password_label = tk.Label(master=self._frame, text="Password")
        password_label.pack()

        self.password_entry = tk.Entry(master=self._frame, show="*")
        self.password_entry.pack(fill=tk.X)

        login_button = tk.Button(
            master=self._frame, text="LOGIN", command=self._check_login)
        login_button.pack(pady=10)

        no_user_label = tk.Label(
            master=self._frame, text="Have no username? Create one.")
        no_user_label.pack(pady=10)

        create_user_button = tk.Button(
            master=self._frame, text="CREATE NEW USER", command=self._press_create_new_user)
        create_user_button.pack(pady=5)
