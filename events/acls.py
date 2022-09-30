from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_photo(city, state):
    headers = {"Authorization": PEXELS_API_KEY}
    payload = {"per_page": 1, "query": city + " " + state}
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params=payload, headers=headers)
    content = json.loads(response.content)
    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except:
        return {"picture_url": None}


def get_weather_data(city, state):
    # headers = {"Authorization": OPEN_WEATHER_API_KEY}
    # Create the URL for the geocoding API with the city and state
    # Make the request
    # Parse the JSON response
    # Get the latitude and longitude from the response

    # Create the URL for the current weather API with the latitude
    #   and longitude
    # Make the request
    # Parse the JSON response
    # Get the main temperature and the weather's description and put
    #   them in a dictionary
    # Return the dictionary
    payload = {"q": f"{city}, {state}", "appid": OPEN_WEATHER_API_KEY}
    url = "http://api.openweathermap.org/geo/1.0/direct"
    response = requests.get(url, params=payload)
    content = json.loads(response.content)
    try:
        lat = content[0]["lat"]
        lon = content[0]["lon"]
    except:
        lat = None
        lon = None

    payload2 = {"lat": lat, "lon": lon, "appid": OPEN_WEATHER_API_KEY}
    url2 = "https://api.openweathermap.org/data/2.5/weather"
    response2 = requests.get(url2, params=payload2)
    content2 = json.loads(response2.content)
    try:
        return {
            "temp": content2["main"]["temp"],
            "description": content2["weather"]["description"],
        }
    except:
        return {"temp": None, "description": None}
