import requests


class World_wheather:
    def __init__(self):
        self.city = input("please fill up your city  : ")
        self.BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
        self.API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'
        complete_url = self.BASE_URL + "appid=" + self.API_KEY + "&q=" + self.city
        response = requests.get(complete_url)
        self.r_data = response.json()

    def calcul(self):
        if self.r_data["cod"] != "404":
            y = self.r_data['main']
            current_t = y['temp']
            current_p = y["pressure"]
            z = self.r_data["weather"]
            weather_description = z[0]["description"]
            answer = f"temp = {str((round(current_t - 273.15)))}C \npressure = {str(current_p)}Br \ndescription = {weather_description}"
            return answer
        else:
            return 'city not found'


if __name__ == '__main__':
    one = World_wheather()
    print(one.calcul())

"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать модуль test_wheather.py  внутри создать Класс для тестирования функции, с помощью unittest.
mock, patch
"""
