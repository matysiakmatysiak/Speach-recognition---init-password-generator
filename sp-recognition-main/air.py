import requests
import json

def air_condition():
    response = requests.get("https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.5235&longitude=13.4115&hourly=pm10,pm2_5&domains=cams_europe&timezone=Europe%2FLondon")

    if (response.status_code != requests.codes.ok):
        print('coś poszło nie tak')
    else:
        print(response.json())
        f = open('air.json', mode='a', encoding='UTF8')
        f.write(f'air condition = {response.json()}\n')
        f.close