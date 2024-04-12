# data_fetcher.py
import requests

PREFIX = 'https://api.openweathermap.org/data/2.5'

class DataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather(self, city):
        try:
            payload = {
                'q': city,
                'APPID': self.api_key,
                'units': 'metric'
            }
            response = requests.get(f'{PREFIX}/weather', params=payload)

            return response.text
        except:
            print('API를 호출하는 도중 문제가 발생하였습니다.')
