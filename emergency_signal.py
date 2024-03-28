import time
import random
import uuid

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

def generate_sample_data(drone_id):
    return {
        "drone_id": drone_id,
        "latitude": round(random.uniform(12.0, 13.0), 6),
        "longitude": round(random.uniform(77.0, 78.0), 6),
        "altitude": round(random.uniform(50, 100), 2),
        "emergency_type": random.choice(["Medical Emergency", "Fire Emergency", "Natural Disaster"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "uuid": str(uuid.uuid4())  # Adding a UUID for uniqueness
    }

def simulate_emergency(drone_id):
    drone = Drone(drone_id)
    drone.send_emergency_signal()
    data = generate_sample_data(drone_id)
    drone.transmit_data(data)

# Simulate emergency signals from multiple drones
NUM_DRONES = 5
for i in range(NUM_DRONES):
    simulate_emergency(i+1)

