import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json


broker='o73c6c14.ala.us-east-1.emqxsl.com'
topic="gw/#"
client = MongoClient("mongodb://localhost:27017/")
x=[]
y=[]


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, message):
    print("received data is :")  
    res = json.loads(str(message.payload.decode("utf-8")))
    print (res)
    with open ("dataCollect.json", "w") as outfile:
       json.dump(res, outfile)
    print("")

def graph_measure():
    filter={
        'mac': 'AC233FA4D283'
    }
    project={
        'temperature': 1, 
        'timestamp': 1, 
        'humidity': 1,
        '_id': 0
    }
    result = client['Labo3']['dataCollect'].find(
        filter=filter,
        projection=project
    )

    for ti in result:
        x.append(ti['timestamp'])
        y.append(ti['temperature'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("TSO3", "TgE")
client.tls_set()
client.connect(broker, 8883, 60)
client.loop_start()