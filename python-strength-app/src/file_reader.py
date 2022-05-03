import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass


squat_file_path = os.path.join(dirname, "..", "data", "squat.csv")
deadlift_file_path = os.path.join(dirname, "..", "data", "deadlift.csv")
bench_press_file_path = os.path.join(dirname, "..", "data", "benchpress.csv")
shoulder_press_file_path = os.path.join(dirname, "..", "data", "shoulderpress.csv")
pull_up_file_path = os.path.join(dirname, "..", "data", "pullup.csv")

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
