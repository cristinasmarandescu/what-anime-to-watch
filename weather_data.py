import requests
import os

OWM_API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,hourly,alerts"
}


class WeatherData:

    def get_weather_id(self):
        """
        Gets the weather id using the Open Weather Map API.

        """
        response = requests.get(url=OWM_Endpoint, params=weather_params)
        response.raise_for_status()
        weather_data = response.json()
        weather_id = weather_data["daily"][0]["weather"][0]["id"]

        return weather_id

    def determine_genre(self, weather_id):
        """
        Determines a genre list for the anime based on the weather id.
        """
        genre = []
        if weather_id < 300:
            genre.extend(["Horror", "Drama"])
        elif 300 <= weather_id < 700:
            genre.extend(["Romance", "Slice of Life", "Suspense", "Comedy"])
        elif 700 <= weather_id < 800:
            genre.extend(["Mystery", "Supernatural", "Fantasy"])
        else:
            genre.extend(["Action", "Sports", "Adventure"])

        return genre
