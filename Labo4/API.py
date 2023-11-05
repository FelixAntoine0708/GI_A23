from fastapi import FastAPI
import DATA as data
import uvicorn
import threading as th
import SQL as sql
app =''
thread =0


data.main() # get the inforamtion on the tags

### Create the 3 information for the tags ###
tag1 = {"name": data.allDevice[0], "time":data.allMessage[0]['timestamp'], "MAC adress":data.allMessage[0]['mac'], "Signal Strenght":data.allMessage[0]['rssi'], "Battery Level": data.allInfo[0].battery, "Acceleration":{"X":data.allInfo[0].x,"Y":data.allInfo[0].y,"Z":data.allInfo[0].z}}
tag2 = {"name": data.allDevice[1], "time":data.allMessage[1]['timestamp'], "MAC adress":data.allMessage[1]['mac'], "Signal Strenght":data.allMessage[1]['rssi'], "Battery Level": data.allInfo[1].battery, "Acceleration":{"X":data.allInfo[1].x,"Y":data.allInfo[1].y,"Z":data.allInfo[1].z}}
tag3 = {"name": data.allDevice[2], "time":data.allMessage[2]['timestamp'], "MAC adress":data.allMessage[2]['mac'], "Signal Strenght":data.allMessage[2]['rssi'], "Battery Level": data.allMessage[2]['battery'], "Temperature": data.allMessage[2]['temperature'],"Humidity": data.allMessage[2]['humidity']}

"""
*   il sert a faire la page API et a prendre les donnée
*   et les mettre dans une base de donnée SQL 
"""
def apiPage():
    global app
    global thread
    app = FastAPI()

    

    @app.get("/")
    async def root():
        return tag1, tag2, tag3
    if __name__ == 'API':
        thread = th.Thread(target=sql.sql_choice)
        thread.start()
        uvicorn.run(app)