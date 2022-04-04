import tkinter as tk
from login_view import LoginView
from create_new_user import CreateNewUser

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
        
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _press_create_new_user(self):
        self._show_create_new_user_view()

    def _press_login(self):
        self._show_x_view()
    
    def _press_back_to_login(self):
        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._press_create_new_user
        )

        self._current_view.pack()

    def _show_create_new_user_view(self):
        self._hide_current_view()

        self._current_view = CreateNewUser(
            self._root,
            self._press_back_to_login
        )

        self._current_view.pack()

window = tk.Tk()
window.title("StrengthApp")

ui = UI(window)
ui.start()

window.mainloop()
