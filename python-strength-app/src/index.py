import tkinter as tk
from ui.ui import UserInterface


def main():
    window = tk.Tk()
    window.title("StrengthApp")

    user_interface = UserInterface(window)
    user_interface.start()

    window.mainloop()


if __name__ == '__main__':
    main()
