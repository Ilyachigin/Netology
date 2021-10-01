import requests


class YandexFolder:

    def __init__(self):
        token = ''
        self.host = 'https://cloud-api.yandex.net:443'
        self.headers = {"Content-type": "application/json",
                        "Authorization": token}

    def new_folder(self):
        response = requests.put(self.host + '/v1/disk/resources?path=test', headers=self.headers)
        return response

    def folder_info(self):
        response = requests.get(self.host + '/v1/disk/resources?path=test', headers=self.headers)
        return response




