import tkinter as tk
from services.user_service import user_service
import datetime


class ExerciseListView:
    """Harjoitusten valikosta vastaava näkymä."""

    def __init__(self, root, press_back_to_login, press_squat, press_deadlift, press_bench_press, press_shoulder_press, press_pull_up, press_calendar):
        """Luokan konstruktori, joka luo harjoituslista-näkymän.

        Args:
            root:
                TKinter-elementti, joka vastaa Tkinter-ikkunasta.
            press_back_to_login:
                Kutsuttava arvo, jolla siirrytään takaisin kirjautumisnäkymään.
            press_squat:
                Kutsuttava arvo, jolla siirrytään squat(kyykky)-näkymään.
            press_deadlift:
                Kutsuttava arvo, jolla siirrytään deadlift(maastaveto)-näkymään.
            press_bench_press:
                Kutsuttava arvo, jolla siirrytään bench_press(penkkipunnerrus)-näkymään.
            press_shoulder_press:
                Kutsuttava arvo, jolla siirrytään shoulder_press(pystypunnerrus)-näkymään.
            press_pull_up:
                Kutsuttava arvo, jolla siirrytään pull_up(leuanveto)-näkymään.
            press_calendar:
                Kutsuttava arvo, jolla siirrytään kalenteri-näkymään.
        """
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._press_back_to_login = press_back_to_login
        self._press_squat = press_squat
        self._press_deadlift = press_deadlift
        self._press_bench_press = press_bench_press
        self._press_shoulder_press = press_shoulder_press
        self._press_pull_up = press_pull_up
        self._press_calendar = press_calendar
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=tk.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        user_label = tk.Label(
            master=self._frame, text=f"Logged in as:   {self._user.username}"
        )
        user_label.pack()

        today_date = datetime.datetime.now().date()
        today_date_reformat = today_date.strftime("%d.%m.%Y")
        date_label = tk.Label(
            master=self._frame, text=f"Date today:    {today_date_reformat}"
        )
        date_label.pack()

        back_button = tk.Button(
            master=self._frame, text="BACK TO LOGIN", command=self._press_back_to_login)
        back_button.pack(pady=10)

        intro_text = tk.Label(
            master=self._frame, text="Choose your exercise.", font=("Arial", 10, "bold"))
        intro_text.pack(side=tk.TOP, anchor=tk.NW, pady=15)

        squat_button = tk.Button(
            master=self._frame, text="SQUAT", command=self._press_squat)
        squat_button.pack(pady=2, side=tk.TOP, anchor=tk.NW)

        deadlift_button = tk.Button(
            master=self._frame, text="DEADLIFT", command=self._press_deadlift)
        deadlift_button.pack(pady=2, side=tk.TOP, anchor=tk.NW)

        bench_press_button = tk.Button(
            master=self._frame, text="BENCH PRESS", command=self._press_bench_press)
        bench_press_button.pack(pady=2, side=tk.TOP, anchor=tk.NW)

        shoulder_press_button = tk.Button(
            master=self._frame, text="SHOULDER PRESS", command=self._press_shoulder_press)
        shoulder_press_button.pack(pady=2, side=tk.TOP, anchor=tk.NW)

        pull_up_button = tk.Button(
            master=self._frame, text="PULL UP", command=self._press_pull_up)
        pull_up_button.pack(pady=2, side=tk.TOP, anchor=tk.NW)

        calendar_text = tk.Label(
            master=self._frame, text="Calendar", font=("Arial", 10, "bold"))
        calendar_text.pack(side=tk.TOP, anchor=tk.N, pady=15)

        calendar_button = tk.Button(
            master=self._frame, text="Open calendar", command=self._press_calendar)
        calendar_button.pack(pady=2, side=tk.TOP, anchor=tk.N)
