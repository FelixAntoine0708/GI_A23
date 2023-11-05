import sqlite3 as sql

dbsql = sql.connect("testLabo3.db")
cur = dbsql.cursor()
#cur.execute("CREATE TABLE test(city, actual_temp, temp_min, temp_max, humidity, wind_speed)")
sql_actual = """
    INSERT INTO test
        (actual_temp, temp_min, temp_max, humidity, wind_speed,city)
    VALUES
        (?, ?, ?, ?, ?, ?)
"""
show =""

def sql_choice(sqlData):
    global show

    actual_temp = sqlData['main']['temp']
    max_temp = sqlData['main']['temp_max']
    min_temp = sqlData['main']['temp_min']
    humidity = sqlData['main']['humidity']
    wind_speed = sqlData['wind']['speed']
    location = sqlData['name']
    cityWeather= (actual_temp, min_temp, max_temp, humidity, wind_speed,location)
    cur.execute(sql_actual, cityWeather)
    dbsql.commit()
    show = cur.execute("SELECT actual_temp, humidity, city FROM test ORDER BY rowid DESC LIMIT 1").fetchall()