import requests
from pprint import pprint
from datetime import datetime, date, timedelta


""" Задание №1, СуперГерои """


class SuperHero():
    def __init__(self, name):
        self.name = name

    def get_request_intelligence(self):
        url = 'https://superheroapi.com/api/2619421814940190/search/' + self.name
        shero_info = requests.get(url)
        stats = shero_info.json()
        intelligence = stats['results'][0]['powerstats']['intelligence']
        return intelligence


name_shero = ['Hulk', 'Captain America', 'Thanos']
shero_inteligence = {}
for hero in name_shero:
    hero = SuperHero(hero)
    shero_inteligence[hero.name] = hero.get_request_intelligence()
pprint(max(shero_inteligence))


""" Задание №2 Работа с Яндекс API"""


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'content-type': 'aplication/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': file_path, 'overwrite': 'true'}
        res = requests.get(url, headers=headers, params=params)
        href = res.json().get('href', ' ')
        response = requests.put(href, data=open('text.txt', 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

path_to_file = os.path.join('/request', 'text.txt')
token = ''
uploader = YaUploader(token)
result = uploader.upload(path_to_file)


""" Задача №3. Необязательная но интересная! """

url = 'https://api.stackexchange.com/2.3/questions'
today = date.today()
need_day = today - timedelta(days=2)
params = {'fromdate': need_day,
          'tagged': 'python',
          'order': 'desc',
          'sort': 'creation',
          'site': 'stackoverflow',
          }
stackoverflow_result = requests.get(url, params=params)

