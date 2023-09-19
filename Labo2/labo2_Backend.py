import paho.mqtt.client as paho
import json
from pymongo import MongoClient
from pprint import pprint as pp
import os

broker='192.219.68.143'  #host name
topic="gw/#"
client = MongoClient("mongodb://localhost:27017/")
db = client["Labo2"]
Collection = db["data"]
measure = 0

     
def on_message(client, userdata, message):
    print("received data is :")  
    res = json.loads(str(message.payload.decode("utf-8")))
    print (res)


    with open ("data.json", "w") as outfile:
       json.dump(res, outfile)

    print("")

    with open ('data.json') as file:
       file_data = json.load(file)

    if isinstance(file_data, list):
        Collection.insert_many(file_data) 
    else:
        Collection.insert_one(file_data)
    
client= paho.Client("user") #create client object 
client.on_message=on_message

print("connecting to broker host",broker)
client.connect(broker)#connection establishment with broker
print("subscribing begins here")    
client.subscribe(topic)#subscribe topic test

while 1:
 client.loop_start() #contineously checking for message 