import requests
key = '0a65a858315b421782e2f12cebd5b3d5'
mainUrl = "https://api.rawg.io/api/"
def getData(url="",querrys=""):
    return requests.get(f"{mainUrl}{url}?key={key}&{querrys}").json()

def getGamByName(name):
    return getData(url="games",querrys=f"search={name}")['results'][0]
def getGameByID(id):
    return getData(url=f"games/{id}",querrys="")
def getGameDescriptionbyName(name):
    result = getGamByName(name)
    game = getGameByID(result['id'])
    return game
