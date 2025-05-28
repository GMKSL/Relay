import time
import random

# ------------------ SENSOR ------------------
def simulate_data():
    return {
        "device": random.choice(["Smart Light", "Smart Fan", "Smart AC"]),
        "power_watts": round(random.uniform(10, 100), 2),
        "unit": "W",
        "status": random.choice(["ON", "OFF"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }