import Labo3_API as api
import labo3_SQL as sql
import labo3_frontend as front
city = "Quebec"

def change():
    global city
    api.weathermap_result(city)
    city = front.select_city
    sql.sql_choice(api.sqlData)
    front.window.after(100,change)

front.button(api.weathermap_result,sql.sql_choice)
#front.graph()
change()
front.window.mainloop()