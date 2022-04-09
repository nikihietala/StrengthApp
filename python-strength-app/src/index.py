import tkinter as tk
from ui.ui import UI


def main():
    window = tk.Tk()
    window.title("StrengthApp")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
