from datetime import datetime
import requests
def request():
    params = {
        "access_key" : "fbc87b3f8797b3fbccb22f7e611daefb",
        "query" : "Kolkata"
        # 'lat' : 22.570,
        # 'lon': 88.370
    }
    response = requests.get("http://api.weatherstack.com/current?", params = params).json()

    time = response["location"]["localtime"]
    temperature = response["current"]["temperature"]
    humidity = response["current"]['humidity']
    wind_speed = response["current"]['wind_speed']
    # time = datetime.strptime(response["hourly"]["time"][0],"%Y-%m-%dT%H:%M"),
    # temperature = response["hourly"]["temperature_2m"][0]
    # relative_humidity = response["hourly"]["relativehumidity_2m"][0]
    # windspeed = response["hourly"]["windspeed_10m"][0]

    return ([time,temperature,humidity,wind_speed])


if __name__ == "__main__":
    print(request())