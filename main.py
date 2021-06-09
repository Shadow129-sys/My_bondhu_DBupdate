import config
import time
from pymongo import MongoClient
from pprint import pprint
from random import seed
from random import randint
from datetime import datetime
from geoLocate_class import geoLocate
import pytz


class Posts:
    def __init__(self, olddata, newCollection):
        self.uid = ""
        self.olddata = olddata
        while(1):
            self.generateuid()
            if(newCollection.find({"uid": self.uid}).count() == 0):
                break
            self.uid = ""

    def generateuid(self):
        self.uidParts(8)
        self.uid += '-'
        self.uidParts(4)
        self.uid += '-'
        self.uidParts(4)
        self.uid += '-'
        self.uidParts(4)
        self.uid += '-'
        self.uidParts(12)

    def uidParts(self, length: int):
        uid = ""
        while(len(uid) < length):
            num = randint(0, 122)
            if(num >= 97):
                num = chr(num)
            else:
                num = str(num)
            uid += num
        for i in range(0, length):
            self.uid += uid[i]

    def Build(self):
        self.ob = geoLocate(self.olddata["hospital_name"])
        self.dataEntry = {
            "uid": self.uid,
            "Address": {
                "Location": {
                    "type": "Point",
                    "coordinates": self.ob.fetchCoordinates()
                },
                "StreetAddress": {
                    "State": "West Bengal",
                    "District": self.olddata["district"],
                    "City": ""
                }
            },
            "Beds": {
                "ICU": self.olddata["available_icu_beds_without_ventilator"] + self.olddata["available_icu_beds_with_ventilator"],
                "Normal": self.olddata["available_beds_allocated_to_covid"] + self.olddata["available_beds_without_oxygen"]
            },
            "CovidVaccines": {
                "Available": False,
                "VaccineName": "",
                "Quantity": 0
            },
            "CreatorEmail": "gsayankr02@gmail.com",
            "Doctors": 0,
            "Email": "",
            "FacilityName": self.olddata["hospital_name"],
            "Oxygen": self.olddata["available_beds_with_oxygen"],
            "PhoneNumber": self.olddata["hospital_phone"],
            "__v": 0,
            "createdAt": datetime.now(pytz.timezone('Asia/Kolkata')),
            "updatedAt": datetime.now(pytz.timezone('Asia/Kolkata'))
        }

    def Data(self):
        return self.dataEntry

    def show(self):
        print("Current uid: "+self.uid)


if __name__ == "__main__":
    cluster = MongoClient(config.mongoClient)
    db = cluster[config.clusterName]
    Oldcollection = db[config.collectionName]
    Newcollection = db[config.collectionNameNew]
    olddataEntries = Oldcollection.find({})
    for olddata in olddataEntries:
        ob = Posts(olddata, Newcollection)
        ob.Build()
        ob.show()
        Newcollection.insert_one(ob.Data())
        time.sleep(10)
