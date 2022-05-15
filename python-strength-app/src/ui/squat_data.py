from csv import *
import tkinter as tk
from file_reader import squat_file_path
from services.user_service import user_service
from repositories.exercise_repository import ExerciseRepository


class SquatData:
    """Kyykky-tulosten tarkastelua vastaava näkymä."""
    def __init__(self, root, press_login):
        """Luokan konstruktori. Luo kyykky-tulosten tarkastelunäkymän.

        Args:
            root:
                TKinter-elementti, joka vastaa Tkinter-ikkunasta.
            press_login:
                Kutsuttava arvo, jolla siirrytään takaisin sovelluksen harjoituslistanäkymään.
        """
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._press_login = press_login
        self._squat_file_path = squat_file_path
        self._user_data = ExerciseRepository()._user_data
        ExerciseRepository.read_squat(self)
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=tk.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        back_button = tk.Button(
            master=self._frame, text="BACK TO EXERCISE LIST", command=self._press_login)
        back_button.pack(pady=10)

        squat_text = tk.Label(master=self._frame, text="Squat results")
        squat_text.pack(side=tk.TOP, anchor=tk.NW)

        var = tk.StringVar(value=self._user_data)
        listbox = tk.Listbox(master=self._frame,
                                listvariable=var, width=30)
        listbox.pack()
        max_squat_text = tk.Label(master=self._frame, text=f"Your maximum weight in squat is: {self.max_squat_weight} kg")
        max_squat_text.pack(side=tk.TOP, anchor=tk.NW)
