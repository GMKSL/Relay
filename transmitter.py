import time
import random
import json
import os
import csv
from datetime import datetime
import requests
from flask import Flask, request, jsonify
import threading
from storage.local_storage import store_data_to_csv

# ------------------ CONFIG ------------------
HOST = '127.0.0.1'
RECEIVER_PORT = 5000
MONITOR_PORT = 12346
LOG_FILE = os.path.join(os.path.dirname(__file__), '../Simulator_log.txt')

monitor_conn = None

app = Flask(__name__, template_folder='../templates')

# ------------------ VALIDATION ------------------
def validate_data(data):
    try:
        if not all(k in data for k in ["device", "power_watts", "unit", "status", "timestamp"]):
            return False
        datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
        if data["unit"] != "W" or data["status"] not in ["ON", "OFF"]:
            return False
        return True
    except Exception:
        return False

        
        
# ------------------ RECEIVER ------------------
def receiver_server():
    try:
    	with open(LOG_FILE, 'a') as logfile:
        	app.run(host='127.0.0.1', port=RECEIVER_PORT)
    except Exception as e:
        print(f"[RECEIVER] Error: {e}")
        logfile.write(f"[RECEIVER] Error: {e}")
        

@app.route('/sensor_data', methods=['POST'])
def handle_sensor_data():
    try:
    	with open(LOG_FILE, 'a') as logfile:
	        time.sleep(random.uniform(0.1, 2.0))  # Simulated network latency
	        data = request.json
	        if validate_data(data):
	            print("[RECEIVER] Valid data received:", data)
	            logfile.write(f"[RECEIVER] Valid data received:{data}"+'\n')
	            store_data_to_csv(data)
	            if monitor_conn:
	                monitor_conn.sendall(json.dumps(data).encode())
	            return jsonify({"status": "success"}), 200
	        else:
	            print("[RECEIVER] Invalid data received.")
	            logfile.write(f"[RECEIVER] Valid data received:" + '\n')
	            return jsonify({"status": "error", "message": "Invalid data"}), 400
    except Exception as e:
        print(f"[RECEIVER] Error processing data: {e}")
        logfile.write(f"[RECEIVER] Error processing data: {e}+ '\n'")
        return jsonify({"status": "error", "message": "Error processing data"}), 500
        
    
