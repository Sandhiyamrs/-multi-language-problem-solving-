import requests

city = input("Enter city: ")
try:
    url = f"http://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    current = data['current_condition'][0]
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['windspeedKmph']} km/h")
    print(f"Feels like: {current['FeelsLikeC']}°C")
except Exception as e:
    print("Error fetching weather:", e)
