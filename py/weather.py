# api key 51857bc1f39669d175e5428e6995976d
# https://openweathermap.org/find?utf8=%E2%9C%93&q=Stavropol
# Stavropol’, RU
# [45.0428, 41.9733]

# man - https://pypi.org/project/pyowm/

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

try:
    owm = OWM('51857bc1f39669d175e5428e6995976d')
    mgr = owm.weather_manager()
    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    #place = input("Введите город: ")
    #place = 'Stavropol’,RU'
    place = input("Введите название населенного пунта: ")
    if place == '':
        place = 'Ставрополь'

    obs = mgr.weather_at_place(place)

    w = obs.weather
    #print (w)

    #temp = w.temperature('celsius')["temp"]
    #windspeed = w.wind()["speed"]
    #winddeg = w.wind()['deg']
    winddirections = ("северный", "северо-восточный", "восточный", "юго-восточный", "южный", "юго-западный", "западный", "северо-западный")
    direction = int((w.wind()['deg'] + 22.5) // 45 % 8)
    #print(winddirections[direction])

    print(f'В городе {place} сейчас:')
    print(f'облачность:  {w.detailed_status} ({w.clouds }%)')
    print(f'температура: {str(round(w.temperature('celsius')["temp"]))}℃')
    print(f'ветер:       {str(round(w.wind()["speed"]))} м/с, {winddirections[direction]} ({w.wind()["deg"]}°)')
    print(f'влажность:   {w.humidity}%')
    print(f'дождь:       {w.rain}')
    #print(f'УФ индекс:   {w.heat_index}')

    total = f'В городе {place} сейчас: {w.detailed_status}, {str(round(w.temperature('celsius')["temp"]))}℃, ветер {str(round(w.wind()["speed"]))} м/с, {winddirections[direction]}'
    print(total)

except:
    print("Получить погоду не удалось.")

'''
w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
'''