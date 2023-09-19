import pymongo
import matplotlib.pyplot as plt

broker='192.219.68.143'  #host name
topic="gw/#"    #chemin pour le broker
client = pymongo.MongoClient("mongodb://localhost:27017/")  #emplacement de la banque de données
db = client["Labo2"]    #la banque de données
Collection = db["data"] # emplacement des données
#variables pour les schémas
x1 =[]
x2 =[]
y =[]


"""
*   Fonction qui sert a prendre les mesures dans
*   la banque de données MongoDB.
"""
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
    result = client['Labo2']['data'].find(
        filter=filter,
        projection=project
    )
    
    #disperce les mesures dans les bonnes endroit pour le schémas
    for x in result:
        x1.append(x['timestamp'])
        x2.append(x['humidity'])
        y.append(x['temperature'])

"""
*   Fonction qui sert a afficher les mesures prisent
*   dans la banque de données MongoDB dans 2 graphiques 
*   différent.
"""
def show_measurement():
    
    #filtre les mesures par l'adresse MAC
    filter={
        'mac': 'AC233FA4D283'
    }

    get_measurments() #va cherhcer les mesures

    #schémas température
    plt.subplot(2, 1, 1)
    plt.plot(x1,y)
    plt.title ("Temperature from sensor: "+ filter['mac'])
    plt.xlabel("Time")
    plt.ylabel("Temperature")

    #schémas humidity
    plt.subplot(2, 1, 2)
    plt.plot(x2,y)
    plt.title ("humidity from sensor: "+ filter['mac'])
    plt.xlabel("Time")
    plt.ylabel("humidity")

    #montre les 2 schémas
    plt.show()


show_measurement()  #affiche les mesures