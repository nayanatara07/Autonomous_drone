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

    def deliver_relief_supplies(self, supplies):
        """
        Simulate delivering relief supplies to affected areas.

        Parameters:
        - supplies (dict): The relief supplies to deliver.
        """
        print(f"Drone {self.drone_id}: Delivering relief supplies to affected areas...")
        time.sleep(2)
        print(f"Drone {self.drone_id}: Relief supplies delivered successfully.")
        print("Supplies:", supplies)

def generate_relief_supplies(drone_id):
    """
    Generate relief supplies for the drone to deliver.

    Parameters:
    - drone_id (int): The unique identifier of the drone.

    Returns:
    - dict: A dictionary containing relief supplies.
    """
    return {
        "drone_id": drone_id,
        "food": random.randint(10, 100),
        "medical_kits": random.randint(1, 5),
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
    relief_supplies = generate_relief_supplies(drone_id)
    drone.deliver_relief_supplies(relief_supplies)

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



