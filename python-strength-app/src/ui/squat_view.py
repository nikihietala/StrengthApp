import tkinter as tk
from csv import *
from tkinter import messagebox
import datetime
from file_reader import squat_file_path

class SquatView:
    def __init__(self, root, press_login, press_squat_data):
        self._root = root
        self._frame = None
        self._press_login = press_login
        self._press_squat_data = press_squat_data
        self._squat_file_path=squat_file_path
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=tk.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        squat_text = tk.Label(master=self._frame, text="New squat", font=("Arial", 14, "bold"))
        squat_text.pack(side=tk.TOP, pady=1)

        date_text = tk.Label(master=self._frame, text="Date (day.month.year)")
        date_text.pack(pady=2)

        self._date_entry = tk.Entry(master=self._frame)
        self._date_entry.pack(fill=tk.X)
        


        rep_text = tk.Label(master=self._frame, text="Best rep(amount)")
        rep_text.pack(pady=2)

        self._rep_entry = tk.Entry(master=self._frame)
        self._rep_entry.pack(fill=tk.X)



        weight_text = tk.Label(master=self._frame, text="Weight (kg)")
        weight_text.pack(pady=2)

        self._weight_entry = tk.Entry(master=self._frame)
        self._weight_entry.pack(fill=tk.X)

        write_button = tk.Button(master=self._frame, text="SAVE RESULT",command=self._write_to_file)
        write_button.pack(pady=10)

        squat_data_button = tk.Button(master=self._frame, text="PAST RESULTS",command=self._press_squat_data)
        squat_data_button.pack(pady=10)

        back_button = tk.Button(master=self._frame, text="BACK TO EXERCISE LIST",command=self._press_login)
        back_button.pack(pady=10)


    def _write_to_file(self):
        confirmation = messagebox.askquestion("Confirm","You are about to enter the following data\n" + "Date: " + self._date_entry.get() + "\n" + "Best Rep: " + self._rep_entry.get() + "\n" + "Weight: " + self._weight_entry.get())
        if confirmation == 'yes':
            try: 
                datetime.datetime.strptime(self._date_entry.get(), '%d.%m.%Y')
            except ValueError:
                    messagebox.showerror("Cancel","Date has to be in format day.month.year (E.g. 5.4.2022)")
                    return
            if self._weight_entry.get() not in "0123456789":
                messagebox.showerror("Cancel","Weight has to be a positive number")
                return
            if self._rep_entry.get() not in "0123456789":
                messagebox.showerror("Cancel","Best rep has to be a positive number")
                return
            with open(self._squat_file_path,"a",newline='') as file:
                Writer=writer(file)
                Writer.writerow([self._date_entry.get(), self._rep_entry.get() + " reps",self._weight_entry.get() + " kg"])
            messagebox.showinfo("Success","Result saved!")
        else:
            messagebox.showerror("Cancel","Result not saved")
            return


    
        



        





    
