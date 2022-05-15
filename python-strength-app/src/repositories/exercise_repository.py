from csv import *
from file_reader import squat_file_path, deadlift_file_path, bench_press_file_path, shoulder_press_file_path, pull_up_file_path
from services.user_service import user_service



class ExerciseRepository:
    """Käyttäjien kirjaamista harjoitus-tuloksista vastaava luokka."""
    def __init__(self):
        """Luokan konstruktori."""
        self._user = user_service.get_user()
        self._squat_file_path = squat_file_path
        self._deadlift_file_path = deadlift_file_path
        self._bench_press_file_path = bench_press_file_path
        self._shoulder_press_file_path = shoulder_press_file_path
        self._pull_up_file_path = pull_up_file_path
        self._user_data = []
        
        


    def read_squat(self):
        """Käy läpi kyykky-harjoituksen sisällön lukemalla kyseisen csv-tiedoston."""
        with open(self._squat_file_path, "r", newline="") as data:
            Reader = reader(data)
            data = list(Reader)
            self.max_squat_weight = 0
            self.squat_dates = []
            for item in data[1:]:
                if item[3] == f"{self._user.username}":
                    self._user_data.append(item[0:3])
                if int(item[2][:-3]) > self.max_squat_weight:
                    self.max_squat_weight = int(item[2][:-3])
                self.squat_dates.append(item[0])
            

    def read_deadlift(self):
        """Käy läpi maastaveto-harjoituksen sisällön lukemalla kyseisen csv-tiedoston."""
        with open(self._deadlift_file_path, "r", newline="") as data:
            Reader = reader(data)
            data = list(Reader)
            self.max_deadlift_weight = 0
            self.deadlift_dates = []
            for item in data[1:]:
                if item[3] == f"{self._user.username}":
                    self._user_data.append(item[0:3])
                if int(item[2][:-3]) > self.max_deadlift_weight:
                    self.max_deadlift_weight = int(item[2][:-3])
                self.deadlift_dates.append(item[0])

    def read_bench_press(self):
        """Käy läpi penkkipunnerrus-harjoituksen sisällön lukemalla kyseisen csv-tiedoston."""
        with open(self._bench_press_file_path, "r", newline="") as data:
            Reader = reader(data)
            data = list(Reader)
            self.max_bench_press_weight = 0
            self.bench_press_dates = []
            for item in data[1:]:
                if item[3] == f"{self._user.username}":
                    self._user_data.append(item[0:3])
                if int(item[2][:-3]) > self.max_bench_press_weight:
                    self.max_bench_press_weight = int(item[2][:-3])
                self.bench_press_dates.append(item[0])

    def read_shoulder_press(self):
        """Käy läpi pystypunnerrus-harjoituksen sisällön lukemalla kyseisen csv-tiedoston."""
        with open(self._shoulder_press_file_path, "r", newline="") as data:
            Reader = reader(data)
            data = list(Reader)
            self.max_shoulder_press_weight = 0
            self.shoulder_press_dates = []
            for item in data[1:]:
                if item[3] == f"{self._user.username}":
                    self._user_data.append(item[0:3])
                if int(item[2][:-3]) > self.max_shoulder_press_weight:
                    self.max_shoulder_press_weight = int(item[2][:-3])
                self.shoulder_press_dates.append(item[0])

    def read_pull_up(self):
        """Käy läpi leuanveto-harjoituksen sisällön lukemalla kyseisen csv-tiedoston."""
        with open(self._pull_up_file_path, "r", newline="") as data:
            Reader = reader(data)
            data = list(Reader)
            self.max_pull_up_weight = 0
            self.pull_up_dates = []
            for item in data[1:]:
                if item[3] == f"{self._user.username}":
                    self._user_data.append(item[0:3])
                if int(item[2][:-3]) > self.max_pull_up_weight:
                    self.max_pull_up_weight = int(item[2][:-3])
                self.pull_up_dates.append(item[0])


