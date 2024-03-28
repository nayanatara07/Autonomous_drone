import time
import random
import uuid

class Drone:
    """
    Class representing a drone.
    """

    def __init__(self, drone_id):
        """
        Initialize the Drone object.

        Parameters:
        - drone_id (int): The unique identifier of the drone.
        """
        self.drone_id = drone_id

    def send_emergency_signal(self):
        """
        Simulate sending an emergency signal.
        """
        print(f"Drone {self.drone_id}: Sending emergency signal...")
        time.sleep(1)
        print(f"Drone {self.drone_id}: Emergency signal sent.")

    def transmit_data(self, data):
        """
        Simulate transmitting data to nearby transportation service apps.

        Parameters:
        - data (dict): The data to transmit.
        """
        print(f"Drone {self.drone_id}: Transmitting data to nearby transportation service apps...")
        time.sleep(2)
        print(f"Drone {self.drone_id}: Data transmitted successfully.")
        print("Data:", data)

def generate_sample_data(drone_id):
    """
    Generate sample data for the drone.

    Parameters:
    - drone_id (int): The unique identifier of the drone.

    Returns:
    - dict: A dictionary containing sample data.
    """
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
    """
    Simulate an emergency scenario for the drone.

    Parameters:
    - drone_id (int): The unique identifier of the drone.
    """
    drone = Drone(drone_id)
    drone.send_emergency_signal()
    data = generate_sample_data(drone_id)
    drone.transmit_data(data)

def main():
    """
    Main function to simulate emergency signals from multiple drones.
    """
    NUM_DRONES = 5
    print("Initializing drone simulation...")
    for i in range(NUM_DRONES):
        print(f"\nDrone {i+1} activated:")
        try:
            simulate_emergency(i+1)
        except Exception as e:
            print(f"Error encountered for Drone {i+1}: {str(e)}")
    print("\nDrone simulation completed.")

if __name__ == "__main__":
    main()


