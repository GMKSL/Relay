import time
import os
import csv
from datetime import datetime

CSV_FILE = os.path.join(os.path.dirname(__file__), 'sensor_data.csv')

# ------------------ LOCAL STORAGE ------------------
def store_data_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["device_id", "timestamp", "power_consumption"])
        if not file_exists or os.stat(CSV_FILE).st_size == 0:
            writer.writeheader()
        writer.writerow({
            "device_id": data["device"],
            "timestamp": data["timestamp"],
            "power_consumption": data["power_watts"]
        })