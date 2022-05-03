import tkinter as tk
from tkcalendar import *
from services.user_service import user_service
import datetime


class CalendarView:
    def __init__(self, root, press_login):
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._press_login = press_login
        self._initialize()

    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        back_button = tk.Button(
            master=self._frame, text="BACK TO EXERCISE LIST", command=self._press_login)
        back_button.pack(pady=10)

        my_calendar = Calendar(master=self._frame)
        my_calendar.pack(pady=20)
