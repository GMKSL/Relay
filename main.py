import time
import random
import json
import os
import csv
from datetime import datetime
import requests
from flask import Flask, request, jsonify
import threading
from sensors.sensor_reader import simulate_data
from network.transmitter import receiver_server, app
from ui.dashboard import get_sensor_data

# ------------------ CONFIG ------------------
HOST = '127.0.0.1'
RECEIVER_PORT = 5000
MONITOR_PORT = 12346
LOG_FILE = os.path.join(os.path.dirname(__file__), 'Simulator_log.txt')

monitor_conn = None
        
        
# ------------------ PIPELINE ------------------
def sensor_simulator(duration_seconds=60):
    start_time = time.time()
    with open(LOG_FILE, 'a') as logfile:
	    while time.time() - start_time < duration_seconds:
	        try:
	            data = simulate_data()
	            try:
	                if random.random() < 0.1:
	                    raise requests.exceptions.RequestException("Simulated network failure")
	                time.sleep(random.uniform(0.2, 1.5))
	                response = requests.post(f'http://{HOST}:{RECEIVER_PORT}/sensor_data', json=data, timeout=5)
	                if response.status_code == 200:
	                    print(f"[SENSOR] Sent: {data}")
	                    logfile.write(f"[SENSOR] Sent: {data}+ '\n'")
	                else:
	                    print(f"[SENSOR] Failed to send data: {response.status_code}")
	                    logfile.write(f"[SENSOR] Failed to send data: {response.status_code} + '\n'")
	            except requests.exceptions.Timeout:
	                print("[SENSOR] Request timed out. Retrying...")
	                logfile.write("[SENSOR] Request timed out. Retrying...")
	                continue
	            except requests.exceptions.RequestException as e:
	                print(f"[SENSOR] Request failed: {e}")
	                logfile.write(f"[SENSOR] Request failed: {e}+ '\n'")
	            time.sleep(1)
	        except Exception as e:
	            print(f"[SENSOR] Unexpected error: {e}")
	            logfile.write(f"[SENSOR] Unexpected error: {e}+ '\n'")
	            time.sleep(2)
	    print("[SENSOR] Data generation completed.")
	    logfile.write("[SENSOR] Data generation completed.")

# ------------------ MAIN ------------------
if __name__ == "__main__":
    try:
        threading.Thread(target=receiver_server, daemon=True).start()
        time.sleep(3)
        sensor_simulator(duration_seconds=60)
    except KeyboardInterrupt:
        print("Shutting down.")