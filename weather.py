import requests
from tabulate import tabulate

def get_weather(api_key, city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_data = {
                'City': city,
                'Temperature (°C)': data['main']['temp'],
                'Humidity (%)': data['main']['humidity'],
                'Description': data['weather'][0]['description']
            }
            return weather_data
        else:
            print(f"Failed to fetch weather data for {city}: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '5bc55445217d47000757537c112fe465'

    # List of major cities in each state of India
    cities = {
        'Andhra Pradesh': 'Vijayawada',
        'Arunachal Pradesh': 'Itanagar',
        'Assam': 'Guwahati',
        'Bihar': 'Patna',
        'Chhattisgarh': 'Raipur',
        'Goa': 'Panaji',
        'Gujarat': 'Ahmedabad',
        'Haryana': 'Chandigarh',
        'Himachal Pradesh': 'Shimla',
        'Jharkhand': 'Ranchi',
        'Karnataka': 'Bangalore',
        'Kerala': 'Thiruvananthapuram',
        'Madhya Pradesh': 'Bhopal',
        'Maharashtra': 'Mumbai',
        'Manipur': 'Imphal',
        'Meghalaya': 'Shillong',
        'Mizoram': 'Aizawl',
        'Nagaland': 'Kohima',
        'Odisha': 'Bhubaneswar',
        'Punjab': 'Chandigarh',
        'Rajasthan': 'Jaipur',
        'Sikkim': 'Gangtok',
        'Tamil Nadu': 'Chennai',
        'Telangana': 'Hyderabad',
        'Tripura': 'Agartala',
        'Uttar Pradesh': 'Lucknow',
        'Uttarakhand': 'Dehradun',
        'West Bengal': 'Kolkata'
    }

    weather_data = []
    for state, city in cities.items():
        data = get_weather(api_key, city)
        if data:
            weather_data.append(data)

    print(tabulate(weather_data, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()

