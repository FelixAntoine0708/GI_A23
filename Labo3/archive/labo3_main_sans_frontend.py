import labo3_MongoDB as mongo
import labo3_MQTT as mqtt
import labo3_SQL as sql
import Labo3_API as api
import os 
from time import sleep as s

city_name = {"Quebec","Russia","Sweden","Australia","Egypt","Brazil"}
i=0

def showWeather(weather):
    print("Today at "+str(weather[0][2]))
    print("The actual temperature is "+ str(weather[0][0])+"°C")
    print("The humidity is "+str(weather[0][1])+"%")

mqtt.client.loop_forever
mongo.message()
os.system("cls")
while(1):
    print(city_name)
    city= input("select between these five city what weather you want to see\n\r")
    for x in city_name:
        if x == city:
            result = x
        else:
            i+=1

    if i == 5:
        os.system("cls")
        api.weathermap_result(result)
        sql.sql_choice(api.sqlData)
        show = sql.cur.execute("SELECT actual_temp, humidity, city FROM test ORDER BY rowid DESC LIMIT 1").fetchall()
        showWeather(show)
        s(5)
        os.system("cls")

    else:
        os.system("cls")
        print("try to write it without erreur")
        s(5)
        os.system("cls")
        