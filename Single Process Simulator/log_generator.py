import os
import csv
import time
from datetime import datetime


if __name__ == "__main__":
    file_path = f"../Log_Files/run_log.csv"
    # Writing to CSV

    new_data = [
        {
            "Time": 0,
            "Filename": "new image.png",
            "Time_start": time.time(),
            "Time_end": time.time(),
            "Time_Elapsed": time.time(),
            "Rounds": 5,
            "Negative": 0,
        },
    ]
    with open(file_path, mode="a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Time",
                "Filename",
                "Time_start",
                "Time_end",
                "Time_Elapsed",
                "Rounds",
                "Negative",
            ],
        )

        writer.writerows(new_data)


def log_maker(
    filename,
    w,
    h,
    threshold,
    time_start,
    time_end,
    time_elapsed,
    rounds,
    negative
):
    file_path = f"../Log_Files/run_log.csv"
    new_data = [
        {
            "Time": datetime.now(),
            "Filename": filename,
            "Width":w,
            "Height":h,
            "Pixel_Area":w*h,
            "Threshold": threshold,
            "Negative": negative,
            "Time_start": time_start,
            "Time_end": time_end,
            "Time_Elapsed": time_elapsed,
            "Rounds": rounds,

        },
    ]

    file_exists = os.path.isfile(file_path)
    with open(file_path, mode="a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Time",
                "Filename",
                "Width",
                "Height",
                "Pixel_Area",
                "Threshold",
                "Negative",
                "Time_start",
                "Time_end",
                "Time_Elapsed",
                "Rounds",
            ],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerows(new_data)

