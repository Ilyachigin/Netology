import requests

API_TOKEN = '2619421814940190'
URL = 'https://superheroapi.com/api/' + API_TOKEN + '/'


def search(name):
    response = requests.get(URL + 'search/' + name)
    response.raise_for_status()
    return response.json()


def powerstats(data):
    response = requests.get(URL + data['results'][0]['id'] + '/powerstats')
    response.raise_for_status()
    return {"name": response.json()['name'],
            "intelligence": int(response.json()['intelligence'])}


def smartest(hero_1, hero_2, hero_3):
    hero_list = [hero_1, hero_2, hero_3]
    sort_list = sorted(hero_list, key=lambda k: k['intelligence'], reverse=True)
    return sort_list[0]['name']


hulk_data = search('Hulk')
captain_data = search('Captain America')
thanos_data = search('Thanos')

hulk_stats = powerstats(hulk_data)
captain_stats = powerstats(captain_data)
thanos_stats = powerstats(thanos_data)

result = smartest(hulk_stats, captain_stats, thanos_stats)
print('The smartest superhero:', result)

