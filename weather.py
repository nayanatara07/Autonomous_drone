import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, latitude, longitude):
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key,
            'units': 'metric'  # Use metric units for temperature (Celsius)
        }
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description']
                }
                return weather_data
            else:
                print(f"Failed to fetch weather data for {latitude}, {longitude}: {data['message']}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '5bc55445217d47000757537c112fe465'

    # Coordinates for major cities in each state of India
    state_coordinates = {
        'Andhra Pradesh': (15.9129, 79.7400),   # Vijayawada
        'Arunachal Pradesh': (27.1004, 93.6167),  # Itanagar
        'Assam': (26.2006, 92.9376),  # Guwahati
        'Bihar': (25.5941, 85.1376),  # Patna
        'Chhattisgarh': (21.2787, 81.8661),  # Raipur
        'Goa': (15.2993, 74.1240),  # Panaji
        'Gujarat': (22.2587, 71.1924),  # Ahmedabad
        'Haryana': (29.0588, 76.0856),  # Chandigarh
        'Himachal Pradesh': (31.1048, 77.1734),  # Shimla
        'Jharkhand': (23.6102, 85.2799),  # Ranchi
        'Karnataka': (12.9716, 77.5946),  # Bangalore
        'Kerala': (10.8505, 76.2711),  # Thiruvananthapuram
        'Madhya Pradesh': (22.7196, 75.8577),  # Bhopal
        'Maharashtra': (18.5204, 73.8567),  # Mumbai
        'Manipur': (24.8170, 93.9368),  # Imphal
        'Meghalaya': (25.5788, 91.8933),  # Shillong
        'Mizoram': (23.7271, 92.7176),  # Aizawl
        'Nagaland': (25.6667, 94.1167),  # Kohima
        'Odisha': (20.2961, 85.8245),  # Bhubaneswar
        'Punjab': (31.1471, 75.3412),  # Chandigarh
        'Rajasthan': (26.9124, 75.7873),  # Jaipur
        'Sikkim': (27.5330, 88.5122),  # Gangtok
        'Tamil Nadu': (13.0827, 80.2707),  # Chennai
        'Telangana': (17.3850, 78.4867),  # Hyderabad
        'Tripura': (23.9408, 91.9882),  # Agartala
        'Uttar Pradesh': (26.8467, 80.9462),  # Lucknow
        'Uttarakhand': (30.3165, 78.0322),  # Dehradun
        'West Bengal': (22.5726, 88.3639)  # Kolkata
    }

    weather_service = WeatherService(api_key)
    for state, (lat, lon) in state_coordinates.items():
        weather_data = weather_service.get_weather(lat, lon)
        if weather_data:
            print(f"Weather conditions in {weather_data['city']}, {state}:")
            print(f"Temperature: {weather_data['temperature']}°C")
            print(f"Humidity: {weather_data['humidity']}%")
            print(f"Description: {weather_data['description']}")
            print()
        else:
            print(f"Failed to fetch weather data for {state}")

if __name__ == "__main__":
    main()

