import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use metric units for temperature (Celsius)
        }
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                return data
            else:
                print(f"Failed to fetch weather data for {city}: {data.get('message', 'Unknown error')}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def calculate_disaster_probability(weather_data):
    temperature = weather_data.get('main', {}).get('temp', 0)
    humidity = weather_data.get('main', {}).get('humidity', 0)
    wind_speed = weather_data.get('wind', {}).get('speed', 0)
    weather_description = weather_data.get('weather', [{}])[0].get('description', '').lower()

    probability = 0

    if 'thunderstorm' in weather_description or 'storm' in weather_description or 'tornado' in weather_description:
        probability += 0.5
    elif 'rain' in weather_description or 'drizzle' in weather_description:
        probability += 0.3
    elif 'snow' in weather_description or 'blizzard' in weather_description:
        probability += 0.3

    if temperature < 5 or temperature > 35:
        probability += 0.3

    if humidity > 80:
        probability += 0.2

    if wind_speed > 15:
        probability += 0.2

    probability = max(0, min(1, probability))

    return probability

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '5bc55445217d47000757537c112fe465'
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat",
              "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam", "Indore", "Thane", "Bhopal",
              "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad"]

    weather_service = WeatherService(api_key)
    disaster_probabilities = {}

    for city in cities:
        weather_data = weather_service.get_weather(city)
        if weather_data:
            disaster_probabilities[city] = calculate_disaster_probability(weather_data)

    print("Disaster Probabilities:")
    print("| City       | Probability |")
    print("|------------|-------------|")
    for city, probability in disaster_probabilities.items():
        print(f"| {city:<10} | {probability:.2f}        |")

if __name__ == "__main__":
    main()


