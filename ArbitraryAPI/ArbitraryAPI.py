import requests
import json
from datetime import datetime

today = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")

r = requests.get("https://www.gamerpower.com/api/giveaways?platform=steam")
games = json.loads(r.text)

#read last time a chekc was completed
rf = open("lastcheck.txt", "r")
lastcheck = rf.read()
rf.close()

def printGames(games):
    for game in games:
        if game['type'] == "Game" and game['published_date'] > lastcheck: #only show full games since last check
            print(game['title'], '\n', game['open_giveaway_url'], '\n', '\n')
printGames(games)

#write time of last check

wf = open("lastcheck.txt", "w")
wf.write(today)
wf.close()