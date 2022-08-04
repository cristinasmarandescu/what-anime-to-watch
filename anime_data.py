import requests
import json
from random import *
from weather_data import WeatherData

JIKAN_ENDPOINT = "https://api.jikan.moe/v4/top/anime"
JIKAN_PARAMS = {
    "type": "tv",
    "page": 1,
}
#  Each page has 25 anime listings. Change the page to get the next 25 anime listings.


class AnimeData:

    def get_anime_data(self):
        """
        Gets anime data from My Anime List website using Jikan API.
        """
        response = requests.get(url=JIKAN_ENDPOINT, params=JIKAN_PARAMS)
        response.raise_for_status()
        data = response.json()

        return data

    def create_anime_data_json(self):
        """
        Creates a json file with the data received using the get_anime_data function.
        """
        with open("anime_data.json", "w") as data_file:
            json.dump(self.get_anime_data(), data_file, indent=4)

    def get_random_anime(self):
        """
        Returns a random anime from the saved json file or creates a json file if the file doesn't exist.
        Checks if the anime's main genre is part of the genre list set using the weather id.
        If not, the function gets called again.
        """
        # Returns a random anime from the saved json file or creates a json file if the file doesn't exist.
        # Checks if the anime's main genre is part of the genre list set using the weather id.
        try:
            with open("anime_data.json") as data_file:
                anime_data = json.load(data_file)

        except FileNotFoundError:
            self.create_anime_data_json()

        else:
            random_number = randint(0, len(anime_data["data"])-1)
            weather_id = WeatherData().get_weather_id()
            genre = WeatherData().determine_genre(weather_id)

            random_anime = {
                "Name": anime_data["data"][random_number]["title"],
                "Genre": anime_data["data"][random_number]["genres"][0]["name"],
                "Episodes": anime_data["data"][random_number]["episodes"],
                "Score": anime_data["data"][random_number]["score"],
            }

            if random_anime["Genre"] not in genre:
                self.get_random_anime()
            else:
                return random_anime
