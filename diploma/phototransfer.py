import json
import requests
from time import sleep
from urllib import parse
from datetime import datetime

VK_TOKEN = ''


class VkUser:

    def __init__(self, token=VK_TOKEN, version='5.126', user_id=None):
        self.url = 'https://api.vk.com/method/'
        self.token = token
        self.version = version
        self.params = {"access_token": self.token, "v": self.version}
        if user_id:
            self.id = user_id
        else:
            self.id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def profile_photo(self):
        params = self.params.copy()
        params.update({"owner_id": self.id, "album_id": "profile",
                       "count": 5, "extended": True})
        response = requests.get(self.url + 'photos.get', params)
        photo_list = []
        photo_items = response.json()['response']['items']
        for number in range(len(photo_items)):
            print('Фото: ' + photo_items[number]['sizes'][-1:][0]['url'])
            print('Колличество лайков: ' + str(photo_items[number]['likes']['count']) + '\n')
            photo_list.append({'file_name': str(photo_items[number]['likes']['count']),
                               'size': photo_items[number]['sizes'][-1:][0]['type'],
                               'photo': photo_items[number]['sizes'][-1:][0]['url']})
        return photo_list

    def photos_name(self, photo_list):
        name_list = []
        for file in range(len(photo_list)):
            if photo_list[file]['file_name'] + '.jpg' in name_list:
                photo_list[file]['file_name'] = datetime.now().strftime('%Y-%m-%d') + '.jpg'
            else:
                photo_list[file]['file_name'] += '.jpg'
            name_list.append(photo_list[file]['file_name'])
        print('Подготовлены фотографии для загруки: ' + str(name_list))
        return photo_list


class YaUploader:

    def __init__(self, token: str):
        self.token = token
        self.host = 'https://cloud-api.yandex.net:443/'
        self.headers = {"Content-type": "application/json",
                        "Authorization": self.token}

    def folder(self, named_list):
        folder_name = round(datetime.timestamp(datetime.now()))
        response = requests.put(self.host + 'v1/disk/resources?path=' + str(folder_name), headers=self.headers)
        print('\nСоздана папка для загруженных фото: ' + str(response.json()['href']))
        for file in named_list:
            move_url = self.host + 'v1/disk/resources/move?from=' + file['file_name'] + \
                                   '&path=' + str(folder_name) + '%2F' + file['file_name']
            requests.post(move_url, headers=self.headers)
            print(file['file_name'] + ' - перемещен в папку')

    def upload(self, file_list):
        for file in file_list:
            url = self.host + 'v1/disk/resources/upload?path=' + \
                  file['file_name'] + '&url=' + parse.quote(file['photo'])
            upload_response = requests.post(url, headers=self.headers)
            status = False
            while not status:
                response = requests.get(upload_response.json()['href'], headers=self.headers)
                print('\nСтатус загрузки: ' + response.json()['status'])
                if response.json()['status'] == 'in-progress':
                    print('Файл пока не загружен, ожидание...')
                    sleep(5)
                elif response.json()['status'] == 'success':
                    print('Файл %s успешно загружен' % file['file_name'])
                    status = True
                elif response.json()['status'] == 'failed':
                    print(response.json())
                    print('Ошибка при загрузке файла')


if __name__ == '__main__':
    vk_id = input('Введите id пользователя VK: ')
    ya_token = input('Введите token полигона Yandex: ')
    user_1 = VkUser(user_id=vk_id)
    uploader = YaUploader(ya_token)
    photo = user_1.profile_photo()
    named_list = user_1.photos_name(photo)
    uploader.upload(named_list)
    uploader.folder(named_list)
    with open('info.json', 'w') as file:
        file.write(json.dumps(named_list))
    print('\nИнформация о выгруженных файлах находится в info.json')

