from csv import *
import tkinter as tk
from file_reader import deadlift_file_path
from services.user_service import user_service


class DeadliftData:
    def __init__(self, root, press_login):
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._press_login = press_login
        self._deadlift_file_path = deadlift_file_path
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

        deadlift_text = tk.Label(master=self._frame, text="Deadlift results")
        deadlift_text.pack(side=tk.TOP, anchor=tk.NW)

        self._read()

    def _read(self):
        with open(self._deadlift_file_path, "r", newline="") as data:
            Reader = reader(data)
            data = list(Reader)
            user_data = []
            for item in data[1:]:
                if item[3] == f"{self._user.username}":
                    user_data.append(item[0:3])
            var = tk.StringVar(value=user_data)
            listbox = tk.Listbox(master=self._frame,
                                 listvariable=var, width=30)
            listbox.pack()