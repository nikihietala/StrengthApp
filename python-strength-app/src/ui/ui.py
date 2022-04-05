import tkinter as tk
from csv import *
from login_view import LoginView
from create_new_user_view import CreateNewUserView
from exercise_list_view import ExerciseListView
from squat_view import SquatView
from deadlift_view import DeadliftView
from bench_press_view import BenchPressView
from shoulder_press_view import ShoulderPressView
from pull_up_view import PullUpView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
        
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _press_create_new_user(self):
        self._show_create_new_user_view()

    def _press_login(self):
        self._show_exercise_list_view()
    
    def _press_squat(self):
        self._show_squat_view()
    
    def _press_deadlift(self):
        self._show_deadlift_view()
    
    def _press_bench_press(self):
        self._show_bench_press_view()
    
    def _press_shoulder_press(self):
        self._show_shoulder_press_view()
    
    def _press_pull_up(self):
        self._show_pull_up_view()
    
    def _press_back_to_login(self):
        self._show_login_view()
    

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._press_create_new_user,
            self._press_login
        )

        self._current_view.pack()

    def _show_create_new_user_view(self):
        self._hide_current_view()

        self._current_view = CreateNewUserView(
            self._root,
            self._press_back_to_login
        )

        self._current_view.pack()
    
    def _show_exercise_list_view(self):
        self._hide_current_view()

        self._current_view = ExerciseListView(
            self._root,
            self._press_back_to_login,
            self._press_squat,
            self._press_deadlift,
            self._press_bench_press,
            self._press_shoulder_press,
            self._press_pull_up
        )

        self._current_view.pack()
    
    def _show_squat_view(self):
        self._hide_current_view()

        self._current_view = SquatView(
            self._root,
            self._press_login
        )

        self._current_view.pack()
    
    def _show_deadlift_view(self):
        self._hide_current_view()

        self._current_view = DeadliftView(
            self._root,
            self._press_login
        )

        self._current_view.pack()

    def _show_bench_press_view(self):
        self._hide_current_view()

        self._current_view = BenchPressView(
            self._root,
            self._press_login
        )

        self._current_view.pack()

    def _show_shoulder_press_view(self):
        self._hide_current_view()

        self._current_view = ShoulderPressView(
            self._root,
            self._press_login
        )

        self._current_view.pack()      

    def _show_pull_up_view(self):
        self._hide_current_view()

        self._current_view = PullUpView(
            self._root,
            self._press_login
        )

        self._current_view.pack()


window = tk.Tk()
window.title("StrengthApp")

ui = UI(window)
ui.start()

window.mainloop()