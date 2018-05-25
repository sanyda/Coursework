import os
import folium
import json
import pandas as pd
from geopytest import get_cordinates
from class_steam import Get_Steam_player_data


def map_builder(dict_cordinates):
    map1 = folium.Map(location=(0, 0), zoom_start=4)
    for i in dict_cordinates:
        folium.Marker(i, popup="Number of players: "+ str(dict_cordinates[i])).add_to(map1)
    return map1


