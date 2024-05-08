import requests
import datetime
import os, os.path
from json import dumps

############################################################################
# Script to scrape the NY Times strands puzzles from the past 365 days     #
# in order to use them as data (different puzzle every day) :)             #
############################################################################

today = datetime.date.today()
date_list = [today - datetime.timedelta(days=x) for x in range(1500)]
d=0
i=0

while len([f for f in os.listdir('./strands/')]) != 365:
    print(str(date_list[d]))
    response = requests.get(f'https://www.nytimes.com/games-assets/strands/{str(date_list[d])}.json')
    d+=1

    if response.headers.get('content-type') == 'application/json':
        i+=1
        data = response.json()
        with open(f'./strands/{i}.json', "w") as file:
            file.write(dumps(data, indent=4))