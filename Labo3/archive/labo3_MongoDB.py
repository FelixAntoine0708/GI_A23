from pymongo import MongoClient as m
import json
from time import sleep as s

client = m("mongodb://localhost:27017/")
db = client["Labo3"]
Collection = db["dataCollect"]

x1 =[]
y =[]

def message():
    with open ('dataCollect.json') as file:
       file_data = json.load(file)

    if isinstance(file_data, list):
        Collection.insert_many(file_data) 
    else:
        Collection.insert_one(file_data)

def get_measurments():
    
    #filtre les mesures par l'adresse MAC
    filter={
        'mac': 'AC233FA4D283'
    }

    #les mesures qui sontpris de la banque de données
    project={
        'temperature': 1, 
        'timestamp': 1, 
        'humidity': 1,
        '_id': 0
    }

    #met toutes les données dans la variable result
    result = Collection.find(
        filter=filter,
        projection=project
    )
    for x in result:
        x1.append(x['timestamp'])
        y.append(x['temperature'])