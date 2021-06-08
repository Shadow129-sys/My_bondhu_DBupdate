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
        x_coordinate = self.data['results'][0]['geometry']['location']['lat']
        y_coordinate = self.data['results'][0]['geometry']['location']['lng']
        return [x_coordinate, y_coordinate]


if __name__ == '__main__':
    location = "Techno Main Saltlake, Kolkata"
    dir = geoLocate(location)
    coordinates = dir.fetchCoordinates()
    print(coordinates)
