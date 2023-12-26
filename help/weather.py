import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
clear()

import pyowm

owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc")

mg = owm.weather_manager()
obs = mg.weather_at_place('London,GB')
print(obs.weather)


"""
from pyowm.owm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

place = input ("Погода в какой городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

print(w.temperature('celsius'))


w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
"""