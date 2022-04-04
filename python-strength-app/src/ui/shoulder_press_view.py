import tkinter as tk

class ShoulderPressView:
    def __init__(self, root, press_login):
        self._root = root
        self._frame = None
        self._press_login = press_login
        self._initialize()

    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        back_button = tk.Button(master=self._frame, text="BACK TO EXERCISE LIST",command=self._press_login)
        back_button.pack(pady=10)