import tkinter as tk

class CreateNewUser:
    def __init__(self, root, press_back_to_login):
        self._root = root
        self._frame = None
        self._press_back_to_login = press_back_to_login
        self._initialize()

    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        intro_text = tk.Label(master=self._frame, text="Create new username.")
        intro_text.pack(side=tk.TOP, anchor=tk.NW, pady=15)

        username_label = tk.Label(master=self._frame, text="Your username (at least 4 characters long)")
        username_label.pack()

        username_entry = tk.Entry(master=self._frame)
        username_entry.pack(fill=tk.X)


        password_label = tk.Label(master=self._frame, text="Your password (at least 6 characters long)")
        password_label.pack()

        password_entry = tk.Entry(master=self._frame)
        password_entry.pack(fill=tk.X)

        create_button = tk.Button(master=self._frame, text="CREATE",command=self._press_back_to_login)
        create_button.pack(pady=10)