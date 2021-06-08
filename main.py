import config
from pymongo import MongoClient
from pprint import pprint
from random import seed
from random import randint
from datetime import datetime

class Posts:
  def __init__(self):
    self.uid = ""
    self.generateuid()

  def generateuid(self):
    print("generating")
    self.uidParts(8)
    self.uid += '-'
    self.uidParts(4)
    self.uid += '-'
    self.uidParts(4)
    self.uid += '-'
    self.uidParts(4)
    self.uid += '-'
    self.uidParts(12)

  def uidParts(self,length: int):
    uid = ""
    while(len(uid)<length):
      num = randint(0, 122)
      if(num >= 97):
        num = chr(num)
      else:
        num = str(num)
      uid += num
    for i in range(0,length):
      self.uid += uid[i]

  def Build(self):
    self.dataEntry = {
      "uid": self.uid,
      "Address": {
        "Location": {
          "type": "Point",
          "coordinates": [1,1]
        },
        "StreetAddress": {
          "State": "West Bengal",
          "District": "Purulia",
          "City": "Raghunathpur"
        }
      },
      "Beds": {
        "ICU": 20,
        "Normal": 10
      },
      "CovidVaccines": {
        "Available": False,
        "VaccineName": "",
        "Quantity": 0
      },
      "CreatorEmail": "gsayankr02@gmail.com",
      "Doctors": 0,
      "Email": "",
      "FacilityName": "default",
      "Oxygen": 10,
      "PhoneNumber": 9283998133,
      "__v": 0,
      "createdAt": datetime.now(),
      "updatedAt": datetime.now()
    }

  def Data(self):
    return self.dataEntry

  def show(self):
    print("showing")
    print(self.uid)

if __name__ == "__main__":
    cluster = MongoClient(config.mongoClient)
    db = cluster[config.clusterName]
    Oldcollection = db[config.collectionName]
    Newcollection = db[config.collectionNameNew]
    ob = Posts()
    ob.Build()
    pprint(ob.Data())
    Newcollection.insert_one(ob.Data())