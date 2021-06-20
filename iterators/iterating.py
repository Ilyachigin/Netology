import json


class CountryIteration:

    def __init__(self, file):
        self.file = file
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.file):
            raise StopIteration
        country_name = self.file[self.start]['name']['common']
        self.start += 1
        return country_name + ' - https://en.wikipedia.org/wiki/' + country_name.replace(' ', '_')


if __name__ == '__main__':
    with open('countries.json', 'r') as json_file:
        countries_json = json.load(json_file)
    couple = CountryIteration(countries_json)
    with open('wiki.txt', 'w') as wiki:
        for entry in couple:
            wiki.write(str(entry) + '\n')

