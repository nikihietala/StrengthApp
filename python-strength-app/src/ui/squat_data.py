from csv import *
import tkinter as tk
from file_reader import squat_file_path

class SquatData:
    def __init__(self, root, press_login):
        self._root = root
        self._frame = None
        self._press_login = press_login
        self._squat_file_path=squat_file_path
        self._initialize()

    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)



        back_button = tk.Button(master=self._frame, text="BACK TO EXERCISE LIST",command=self._press_login)
        back_button.pack(pady=10)

        squat_text = tk.Label(master=self._frame, text="Squat results")
        squat_text.pack(side=tk.TOP, anchor=tk.NW)

        self._read()
    
    def _read(self):
        with open(self._squat_file_path, "r", newline="") as data:
            Reader=reader(data)
            data=list(Reader)
    
            var = tk.StringVar(value=data[1:])
            listbox=tk.Listbox(master=self._frame, listvariable=var, width=30)
            listbox.pack()