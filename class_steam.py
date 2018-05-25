import urllib.request
import json
class Get_Steam_player_data:
    def __init__(self,id):
        self.api_key = "08A75A4F1E62677F3AC55CD2DC1CF879"
        self.id = str(id)
        self.country = ''
        self.timecreated = ''
        self.lastlogoff = ''
    def getdata(self):
        base_url = " http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" \
                   + self.api_key + "&steamids=" + self.id
        request = urllib.request.Request(base_url)
        with urllib.request.urlopen(base_url) as response:
            data = response.read()

            data = data.decode("utf-8")

            json.loads(data)

        self.country = data.split('"loccountrycode":"')[1][:2]
        self.timecreated = int(data.split('"timecreated":')[1][:10])
        self.lastlogoff = int(data.split('"lastlogoff":')[1][:10])

        return None
