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
                'Description': data['weather'][0]['description'],
                'Wind Speed (m/s)': data['wind']['speed'],
                'Atmospheric Pressure (hPa)': data['main']['pressure'],
                'Weather Condition ID': data['weather'][0]['id']
            }
            return weather_data
        else:
            print(f"Failed to fetch weather data for {city}: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def calculate_disaster_probability(weather_data):
    # Example disaster probability calculation based on weather conditions
    temp_score = 0
    if weather_data['Temperature (°C)'] > 30:
        temp_score += 2
    if weather_data['Humidity (%)'] > 80:
        temp_score += 1
    if weather_data['Weather Condition ID'] in [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]:
        # Thunderstorm conditions
        temp_score += 3
    if weather_data['Weather Condition ID'] in [300, 301, 302, 310, 311, 312, 313, 314, 321]:
        # Drizzle conditions
        temp_score += 1
    if weather_data['Weather Condition ID'] in [500, 501, 502, 503, 504, 511, 520, 521, 522, 531]:
        # Rain conditions
        temp_score += 2
    if weather_data['Weather Condition ID'] in [600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622]:
        # Snow conditions
        temp_score += 2
    if weather_data['Weather Condition ID'] in [701, 711, 721, 731, 741, 751, 761, 762, 771, 781]:
        # Atmospheric conditions
        temp_score += 1
    if weather_data['Wind Speed (m/s)'] > 10:
        temp_score += 2
    if weather_data['Atmospheric Pressure (hPa)'] < 900 or weather_data['Atmospheric Pressure (hPa)'] > 1100:
        temp_score += 2
    
    # Probability score ranges from 0 to 15 (Higher score indicates higher probability of a disaster)
    probability_score = min(temp_score, 15)  # Limit maximum score to 15
    return probability_score

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
            data['Disaster Probability'] = calculate_disaster_probability(data)
            weather_data.append(data)

    print(tabulate(weather_data, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
