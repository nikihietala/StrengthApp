from csv import *
import tkinter as tk
from file_reader import deadlift_file_path
from services.user_service import user_service
from repositories.exercise_repository import ExerciseRepository


class DeadliftData:
    def __init__(self, root, press_login):
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._press_login = press_login
        self._deadlift_file_path = deadlift_file_path
        self._user_data = ExerciseRepository()._user_data
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

        ExerciseRepository.read_deadlift(self)
        var = tk.StringVar(value=self._user_data)
        listbox = tk.Listbox(master=self._frame,
                                listvariable=var, width=30)
        listbox.pack()
        max_deadlift_text = tk.Label(master=self._frame, text=f"Your maximum weight in deadlift is: {self.max_deadlift_weight} kg")
        max_deadlift_text.pack(side=tk.TOP, anchor=tk.NW)
