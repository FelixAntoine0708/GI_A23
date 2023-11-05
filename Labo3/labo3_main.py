import labo3_MongoDB as mongo
import labo3_MQTT as mqtt
import labo3_SQL as sql
import Labo3_API as api
import labo3_frontend as front

mqtt.client.loop_forever
mongo.message()
api.sqlData = api.requests.get('https://api.openweathermap.org/data/2.5/weather?q=Quebec&appid=f24a51704a6b9f8241c7300531bd8622&units=metric').json()
show = sql.cur.execute("SELECT actual_temp, humidity, city FROM test ORDER BY rowid DESC LIMIT 1").fetchall()
sql.sql_choice(api.sqlData)
front.button(api.weathermap_result,sql.sql_choice)

while(1):
    result = front.select_city
    if(result != ''):
        api.weathermap_result(result)
        sql.sql_choice(api.sqlData)