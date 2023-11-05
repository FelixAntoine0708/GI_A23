import requests

sqlData = 0

def weathermap_result(city):
    global sqlData
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=f24a51704a6b9f8241c7300531bd8622&units=metric'
    sqlData = requests.get(url).json()
    