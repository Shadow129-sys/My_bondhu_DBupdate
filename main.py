from geoLocate_class import geoLocate

if __name__ == '__main__':
    location = "DARJEELING DISTRICT HOSPITAL (Government Hospital)"
    dir = geoLocate(location)
    coordinates = dir.fetchCoordinates()
    print(coordinates)
