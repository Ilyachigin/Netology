import requests

URL = 'https://api.vk.com/method/'
VK_TOKEN = ''


class VkUser:

    def __init__(self, token=VK_TOKEN, version='5.126', user_id=None):
        self.token = token
        self.version = version
        self.params = {"access_token": self.token, "v": self.version}
        if user_id:
            self.id = user_id
        else:
            self.id = requests.get(URL + 'users.get', self.params).json()['response'][0]['id']

    def __and__(self, other):
        params = self.params.copy()
        params.update({"source_uid": self.id, "target_uid": other.id})
        response = requests.get(URL + 'friends.getMutual', params)
        return response.json()['response']

    def __str__(self):
        params = self.params.copy()
        params.update({"user_ids": self.id, "fields": 'screen_name'})
        response = requests.get(URL + 'users.get', params)
        return "https://vk.com/" + response.json()['response'][0]['screen_name']

    def mutual_friends(self, target, source=None):
        if source is None:
            source = self.id
        params = self.params.copy()
        params.update({"source_uid": source, "target_uid": target})
        response = requests.get(URL + 'friends.getMutual', params)
        return response.json()['response']


user_1 = VkUser(VK_TOKEN, '5.126')
user_2 = VkUser(user_id=15915271)

user_3 = 15915271
friends_list = user_1.mutual_friends(user_3)  # Task #1
print(friends_list)

print(user_1 & user_2)  # Task #2

print(user_1)  # Task #3

