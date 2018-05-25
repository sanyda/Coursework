from class_steam import Get_Steam_player_data
from geopytest import get_cordinates
from build_map import map_builder
from build_graphic import probability_plot_builder
import time

cordinates = dict()
time_created = set()
last_logoff = set()
for i in range(100):
    try:
        data = Get_Steam_player_data(76561198172378445+i)
        data.getdata()
        if data.country in cordinates:
            cordinates[get_cordinates(data.country)] += 1
        else:
            cordinates[get_cordinates(data.country)] = 1
        time_created.add(data.timecreated)
        last_logoff.add(data.lastlogoff)
    except IndexError:
        pass

map_builder(cordinates).save("map.html")

now = time.time()
time_created_dict = {"more than 5 years ago": 0, "more than 1 year ago": 0, "more than 1/2 year ago": 0, "more than one month": 0,
                     "less than one month": 0}
last_logoff_dict = time_created_dict
for i in time_created:
    if (now - i)/31536000 > 5:
        time_created_dict["more than 5 years ago"] += 1
    elif (now - i)/31536000 > 1:
        time_created_dict["more than 1 year ago"] += 1
    elif (now - i)/31536000 > 0.5:
        time_created_dict["more than 1/2 year ago"] += 1
    elif (now - i)/31536000 > (1/12):
        time_created_dict["more than one month"] += 1
    else:
        time_created_dict["less than one month"] += 1
for i in last_logoff:
    if (now - i)/31536000 > 5:
        last_logoff_dict["more than 5 years ago"] += 1
    elif (now - i)/31536000 > 1:
        last_logoff_dict["more than 1 year ago"] += 1
    elif (now - i)/31536000 > 0.5:
        last_logoff_dict["more than 1/2 year ago"] += 1
    elif (now - i)/31536000 > (1/12):
        last_logoff_dict["more than one month"] += 1
    else:
        last_logoff_dict["less than one month"] += 1

probability_plot_builder(last_logoff_dict,"lastlogoff.png")
probability_plot_builder(time_created_dict,"timecreated.png")







