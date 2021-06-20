import requests

HOST = 'https://cloud-api.yandex.net:443'


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {"Content-type": "application/json",
                   "Authorization": self.token}
        response = requests.get(HOST + '/v1/disk/resources/upload?path=' + file_path[-8:], headers=headers)
        response = requests.put(response.json()['href'], data=open(file_path), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл успешно загружен'


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('/Users/ilyachigin/home/PythonHome/requests/test.txt')
    print(result)

