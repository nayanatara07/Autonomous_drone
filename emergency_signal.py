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

def generate_sample_data(drone_id):
    """
    Generate sample data for the drone.

    Parameters:
    - drone_id (int): The unique identifier of the drone.

    Returns:
    - dict: A dictionary containing sample data.
    """
    states = ["Maharashtra", "Uttar Pradesh", "West Bengal", "Rajasthan", "Madhya Pradesh", "Tamil Nadu", "Karnataka", "Gujarat", "Andhra Pradesh", "Odisha"]
    districts = {
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Allahabad"],
        "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
        "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"],
        "Andhra Pradesh": ["Hyderabad", "Visakhapatnam", "Vijayawada", "Guntur", "Nellore"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur"]
    }
    state = random.choice(states)
    district = random.choice(districts[state])

    return {
        "drone_group": f"Drone Group {drone_id}",
        "people_count": random.randint(1, 10),
        "area_affected": f"{district}, {state}, India",
        "latitude": round(random.uniform(12.0, 13.0), 6),
        "longitude": round(random.uniform(77.0, 78.0), 6),
        "altitude": round(random.uniform(50, 100), 2),
        "emergency_type": random.choice(["Medical Emergency", "Fire Emergency", "Natural Disaster"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "uuid": str(uuid.uuid4())  # Adding a UUID for uniqueness
    }

def simulate_emergency(drone_group_id, num_drones):
    """
    Simulate an emergency scenario for the drone group.

    Parameters:
    - drone_group_id (int): The unique identifier of the drone group.
    - num_drones (int): The number of drones in the group.
    """
    print(f"Drone Group {drone_group_id} activated with {num_drones} drones:")
    for i in range(1, num_drones + 1):
        drone = Drone(f"Drone {drone_group_id}-{i}")
        drone.send_emergency_signal()
        relief_supplies = generate_relief_supplies(f"Drone {drone_group_id}-{i}")
        drone.deliver_relief_supplies(relief_supplies)
        data = generate_sample_data(drone_group_id)
        drone.transmit_data(data)
        print()

def main():
    """
    Main function to simulate emergency signals from multiple drone groups.
    """
    NUM_DRONE_GROUPS = 3
    DRONES_PER_GROUP = 5
    print("Initializing drone simulation...")
    for i in range(1, NUM_DRONE_GROUPS + 1):
        simulate_emergency(i, DRONES_PER_GROUP)
    print("\nDrone simulation completed.")

if __name__ == "__main__":
    main()




