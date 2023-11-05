import sqlite3 as sql
import requests

dbsql = sql.connect("SQLlabo4.db", check_same_thread=False)
cur = dbsql.cursor()
cur.execute("CREATE TABLE tagsData(device, accX, accY, accZ, time, mac, rssi, battery, temperature, humidity)")
sql_actual = """
    INSERT INTO tagsData
        (device, accX, accY, accZ, time, mac, rssi, battery, temperature, humidity)
    VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
device_name=[]


def sql_choice():
    url = "http://127.0.0.1:8000"   
    sqlD = requests.get(url).json() # fait une requete pour avoir tout les information qu'il a de besoins.

    ### met les données dans la basse de données SQL
    for x in range(len(sqlD)):
        device = sqlD[x]['name']
        if device == 'E8 plus':
            accX = sqlD[x]['Acceleration']['X']
            accY = sqlD[x]['Acceleration']['Y']
            accZ = sqlD[x]['Acceleration']['Z']
            time = sqlD[x]['time']
            mac = sqlD[x]['MAC adress']
            rssi = sqlD[x]['Signal Strenght']
            battery = sqlD[x]['Battery Level']
            temperature = 'None'
            humidity = 'None'
            tags= (device, accX, accY, accZ, time, mac, rssi, battery, temperature, humidity)
            cur.execute(sql_actual, tags)
            dbsql.commit()

        else:
            ### si cel ne fonctionne pas et donne une erreur il va essayer l'autre option ###
            try:
                accX = sqlD[x]['Acceleration']['X']
                accY = sqlD[x]['Acceleration']['Y']
                accZ = sqlD[x]['Acceleration']['Z']
                time = sqlD[x]['time']
                mac = sqlD[x]['MAC adress']
                rssi = sqlD[x]['Signal Strenght']
                battery = sqlD[x]['Battery Level']
                temperature = 'None'
                humidity = 'None'
                tags= (device, accX, accY, accZ, time, mac, rssi, battery, temperature, humidity)
                cur.execute(sql_actual, tags)
                dbsql.commit()

            ### si lasolution 1 fait une erreur il va essayer l'exptect ###
            except:
                accX = 'None'
                accY = 'None'
                accZ = 'None'
                time = sqlD[x]['time']
                mac = sqlD[x]['MAC adress']
                rssi = sqlD[x]['Signal Strenght']
                battery = sqlD[x]['Battery Level']
                temperature = sqlD[x]['Temperature']
                humidity = sqlD[x]['Humidity']
                tags= (device, accX, accY, accZ, time, mac, rssi, battery, temperature, humidity)
                cur.execute(sql_actual, tags)
                dbsql.commit()

            ### sinon il imprime que c'est impossible ###
            else: 
                print("this device is weird")
