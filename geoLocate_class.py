import requests
import creds
from pprint import pprint


class geoLocate:
    def __init__(self, location):
        self.location = location
        self.baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
            'address': self.location,
            'key': creds.api_key
        }

    def fetchCoordinates(self):
        self.data = requests.get(self.baseURL, params=self.params).json()
        # pprint(self.data)
        x_coordinate = self.data['results'][0]['geometry']['location']['lng']
        y_coordinate = self.data['results'][0]['geometry']['location']['lat']
        return [x_coordinate, y_coordinate]

    def fetchCity(self):
        pass
