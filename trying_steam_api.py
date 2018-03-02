import urllib.request
import urllib.parse
import json

api_key = "08A75A4F1E62677F3AC55CD2DC1CF879"

def get_data(userid):
    base_url = " http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" \
               + api_key + "&steamids=" + str(userid)
    request = urllib.request.Request(base_url)
    with urllib.request.urlopen(base_url) as response:
        data = response.read()

        data = data.decode("utf-8")

        json.loads(data)

    return data
data = get_data(76561198172378445)
print(data)
