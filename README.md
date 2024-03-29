# Disaster Rescue using Drones

## Introduction

Disaster management is a critical aspect of emergency response, especially in scenarios where human lives are at stake. Drones have emerged as valuable tools in disaster management operations due to their agility, accessibility, and ability to access hard-to-reach areas. This project aims to demonstrate a comprehensive disaster management system utilizing drones for various tasks such as sending emergency signals, delivering relief supplies, assessing affected areas, and detecting people in distress.

## Project Components

### 1. emergency_signal.py

This script simulates drones sending emergency signals to alert transportation systems about affected areas. It includes functionalities to send basic survival food and medical kits to disaster-stricken regions. Each drone group activates multiple drones to cover a wider area efficiently.

### 2. main.py

This script utilizes computer vision to detect the number of people in disaster-affected areas. By analyzing live video feed from a webcam, it counts the number of faces detected, providing crucial information for emergency response teams.

### 3. drone.py

This module implements an autonomous drone capable of executing various tasks. It connects to the drone using the DroneKit library, arms and takes off, scans disaster areas, detects humans using computer vision algorithms, and delivers food packets to identified locations.

### 4. weather.py

This script collects current weather conditions for various cities in India and calculates the probability of having a disaster based on the weather data. It provides valuable information for disaster management operations.

## Usage

To use this project:

1. Ensure all necessary dependencies are installed, including OpenCV, DroneKit, and other required libraries.
2. Run the `emergency_signal.py` script to activate drone groups and simulate emergency signals and relief supply deliveries.
3. Execute the `main.py` script to detect the number of people in disaster-affected areas using computer vision.
4. Utilize the `drone.py` module to deploy autonomous drones for disaster management operations.
5. Run the `weather.py` script to collect weather conditions and assess the probability of disasters in different cities.


## Acknowledgements

We would like to express our gratitude to the open-source community for providing invaluable resources and tools that made this project possible. Additionally, we acknowledge the support and guidance of our mentors and advisors throughout the development process.

- [NayanaTara]