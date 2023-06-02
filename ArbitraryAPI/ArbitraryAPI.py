import requests
import json
from datetime import datetime

lastcheck = ''
def getGames(): #get gamelist, time of last check and record now as the new time of last check
    r = open("lastcheck.txt", "r")
    global lastcheck
    lastcheck = r.read()
    r.close()
    w = open("lastcheck.txt", "w")
    w.write(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"))
    w.close()
    return json.loads(requests.get("https://www.gamerpower.com/api/giveaways?platform=steam").text)

class gamedata: #create a class to store data for each game
    def __init__(self, title, start, end, link):
        self.title = title
        self.start = start
        self.end = end
        self.link = link

def filterGames(games): #select only the games from the list of giveaways and return a list of gamedata objects
    newGames=[]
    oldGames=[]
    for game in games:
        if game['type'] == "Game":
            if datetime.strptime(game['published_date'], "%Y-%m-%d %H:%M:%S") > datetime.strptime(lastcheck, "%Y-%m-%d %H:%M:%S"):
                newGames.append(gamedata(game['title'], game['published_date'], game['end_date'], game['open_giveaway_url']))
            else:
                oldGames.append(gamedata(game['title'], game['published_date'], game['end_date'], game['open_giveaway_url']))
    return newGames, oldGames

def printGames(games):
    for game in games:
        if game['type'] == "Game":
            print(game['title'], '\n', game['open_giveaway_url'], '\n', '\n')