import requests

API_KEY = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Temperature: {temp}°C")
    print(f"Weather: {desc}")
else:
    print("City not found")
