import requests
import json

class WeatherApi:
    def __init__(self, lat, lon, api_key):
        self.lat = lat
        self.lon = lon
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def show_weather(self):
        params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.api_key,
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  
            data = response.json()
            
            city = data["name"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            # print(data)
            
            print(f"The weather in {city} is {desc} with a temperature of {temp}°C.")

        except Exception as e:
            print("Error fetching weather:", e)
            

def main():
    API_KEY = "d31191dabb89522581d14fc39522e6ad"
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    w = WeatherApi(lat, lon, API_KEY)
    w.show_weather()
    
    
while True:
    main()   
    
    
   
