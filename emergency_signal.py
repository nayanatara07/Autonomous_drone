import time
import random

class Drone:
    def __init__(self, drone_id):
        self.drone_id = drone_id

    def send_emergency_signal(self):
        # Simulate sending an emergency signal
        print(f"Drone {self.drone_id}: Sending emergency signal...")
        time.sleep(1)
        print(f"Drone {self.drone_id}: Emergency signal sent.")

    def transmit_data(self, data):
        # Simulate transmitting data to nearby transportation service apps
        print(f"Drone {self.drone_id}: Transmitting data to nearby transportation service apps...")
        time.sleep(2)
        print(f"Drone {self.drone_id}: Data transmitted successfully.")
        print("Data:", data)

def simulate_emergency(drone_id):
    drone = Drone(drone_id)
    drone.send_emergency_signal()
    # Generate sample data to transmit
    data = {
        "latitude": random.uniform(12.0, 13.0),
        "longitude": random.uniform(77.0, 78.0),
        "altitude": random.uniform(50, 100),
        "emergency_type": "Medical Emergency",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    drone.transmit_data(data)

# Simulate emergency signals from multiple drones
for i in range(5):
    simulate_emergency(i+1)
