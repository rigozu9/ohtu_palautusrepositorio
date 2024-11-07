import requests

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def read(self):
        response = requests.get(self._url).json()
        return response
