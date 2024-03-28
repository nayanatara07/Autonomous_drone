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
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description']
                }
                return weather_data
            else:
                print(f"Failed to fetch weather data: {data['message']}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '5bc55445217d47000757537c112fe465'
    latitude = 37.7749  # Example latitude (San Francisco)
    longitude = -122.4194  # Example longitude (San Francisco)

    weather_service = WeatherService(api_key)
    weather_data = weather_service.get_weather(latitude, longitude)
    if weather_data:
        print("Current Weather Conditions:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Description: {weather_data['description']}")

if __name__ == "__main__":
    main()
