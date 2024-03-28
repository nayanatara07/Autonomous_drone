from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the vehicle
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

# Function for arming the drone
def arm_and_takeoff(target_altitude):
    print("Arming motors")
    while not vehicle.is_armable:
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    print("Taking off")
    vehicle.simple_takeoff(target_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {altitude} meters")
        if altitude >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Function for flying to a specific location
def fly_to_location(target_location):
    print(f"Flying to location: {target_location}")
    vehicle.simple_goto(target_location)

# Function for monitoring battery level
def monitor_battery():
    while True:
        battery_level = vehicle.battery.level
        print(f"Battery Level: {battery_level}%")
        if battery_level < 20:
            print("Low battery! Returning home.")
            fly_to_location(vehicle.home_location)
        time.sleep(60)

# Main function
def main():
    try:
        # Arm and takeoff to 10 meters altitude
        arm_and_takeoff(10)

        # Fly to a specific location (example: latitude, longitude, altitude)
        target_location = LocationGlobalRelative(37.773972, -122.431297, 15)
        fly_to_location(target_location)

        # Monitor battery level in the background
        monitor_battery()

    except KeyboardInterrupt:
        print("User interrupted the program")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        print("Exiting...")
        vehicle.close()

if __name__ == "__main__":
    main()

