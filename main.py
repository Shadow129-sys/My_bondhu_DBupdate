import requests
import time
import json
import config
from pprint import pprint


class geoLocate:
    def __init__(self, location):
        self.location = location
        self.baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
            'address': self.location,
            'key': config.api_key
        }

    def fetchCoordinates(self):
        self.data = requests.get(self.baseURL, params=self.params).json()
        pprint(self.data)


if __name__ == '__main__':
    location = "Techno Main Saltlake, Kolkata"
    dir = geoLocate(location)
    dir.fetchCoordinates()