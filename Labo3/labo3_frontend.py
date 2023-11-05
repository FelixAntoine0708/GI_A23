from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Labo3_API as api
import labo3_SQL as sql
import labo3_MQTT as mqtt
from time import sleep as s

city_name= {"Quebec", "Sweden", "Australia", "Russia", "Egypt"}
select_city = ""
window= Tk()
window.title("Labo 3 Graph and city temperature")
window.geometry("800x750")



def button(command_api, command_sql):
    for x in city_name:
        Button(window, text=x, bg="dark grey", command=lambda city =x: [command_api(city), command_sql(api.sqlData),showWeather(sql.show),wich_push(city)]).pack(side=TOP, anchor=NW) # ici s chie peux pas voir plusieurs command

def showWeather(weather):
    print("Today at "+str(weather[0][2]))
    print("The actual temperature is "+ str(weather[0][0])+"°C")
    print("The humidity is "+str(weather[0][1])+"%")

def graph():
    fig, ax = plt.subplots()
    mqtt.graph_measure()
    ax.plot(mqtt.x,mqtt.y)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack

def wich_push(city):
    global select_city
    select_city = city