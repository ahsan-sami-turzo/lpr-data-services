import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/lut-buffet-data")
async def get_lutbuffetdata():
    today = datetime.now().strftime('%Y-%m-%d')
    base_url = "https://api.fi.poweresta.com/publicmenu/dates/kampusravintolat/lut/?menu=syksy&dates="
    url = base_url + today
    response = requests.get(url)
    data = response.json()

    names = []

    for meal_option in data[0]['data']['mealOptions']:
        for row in meal_option['rows']:
            for name in row['names']:
                if name['language'] == 'en':
                    names.append(name['name'])

    # return data[0]['data']['mealOptions']
    return names


@app.get("/api/lut-gym-data")
async def get_gym_data():
    url = 'https://embed.gymplus.fi/v2/light/bold/lutsk'
    response = requests.get(url)
    data = response.json()
    html_content = data['content']
    soup = BeautifulSoup(html_content, 'html.parser')
    realtime_container = soup.find('div', {'id': 'realtime-container'})
    realtime_data = realtime_container.text if realtime_container else "Realtime container data not found"
    numbers = re.findall(r'\d+ / \d+|\d+', realtime_data)
    functional = numbers[3]
    if ' / ' in functional:
        functional = functional.split(' / ')[0]
    gym_data = {
        "people_in_the_gym": numbers[0],
        "muscular_condition_training": numbers[1],
        "aerobic_training": numbers[2],
        "functional_training": int(functional),
    }
    return gym_data


@app.get("/")
async def root():
    return {"message": "Lappeenranta Data Services"}
