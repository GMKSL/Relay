import os
import csv
import os
from flask import Flask, jsonify, render_template
from network.transmitter import app
from datetime import datetime
 
CSV_FILE = os.path.join(os.path.dirname(__file__), '../storage/sensor_data.csv')
 
# Route to get data from the CSV
@app.route('/get_sensor_data', methods=['GET'])
def get_sensor_data():
    try:
        sensor_data = []
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(x.replace('\0', '') for x in file)
            for row in reader:
                sensor_data.append({
                    'timestamp': row['timestamp'],
                    'device_id': row['device_id'],
                    'power_consumption': float(row['power_consumption'])
                })
        return jsonify(sensor_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
# Route to serve the dashboard page
@app.route('/')
def index():
    return render_template('dashboard.html')
