
all_birds = []
all_animals = []


def weight_count(common_list):
    common_weight = []
    for creature in common_list:
        common_weight.append(creature.weight)
    overall_weight = sum(common_weight)
    for creature in common_list:
        if max(common_weight) == creature.weight:
            max_creature = creature.name
    return overall_weight, max_creature


class Animals:

    def __init__(self, animal_type=None, name=None, voice=None):
        self.animal_type = animal_type
        self.name = name
        self.voice = voice

    def feed(self, animal_list=None):
        if animal_list:
            for animal in animal_list:
                print(animal.animal_type, animal.name, 'накормлен')
        else:
            print(self.animal_type, self.name, 'накормлен')


class Birds(Animals):

    def collect_eggs(self):
        print(self.animal_type, self.name, 'собраны яйца')


class Chordate(Animals):

    def milking(self):
        print(self.animal_type, self.name, 'подоена')

    def shearing(self):
        print(self.animal_type, self.name, 'подстрижена')


bird_1 = Birds('гусь', 'Серый', 'гогот')
bird_1.weight = 3.3
bird_1.feed()
bird_1.collect_eggs()
all_birds.append(bird_1)

bird_2 = Birds('гусь', 'Белый', 'гогот')
bird_2.weight = 3.2
bird_2.feed()
bird_2.collect_eggs()
all_birds.append(bird_2)

bird_3 = Birds('курица', 'Ко-Ко', 'кукарекание')
bird_3.weight = 0.8
bird_3.feed()
bird_3.collect_eggs()
all_birds.append(bird_3)

bird_4 = Birds('курица', 'Кукареку', 'кукарекание')
bird_4.weight = 0.7
bird_4.feed()
bird_4.collect_eggs()
all_birds.append(bird_4)

bird_5 = Birds('утка', 'Кряква', 'крякание')
bird_5.weight = 1.5
bird_5.feed()
bird_5.collect_eggs()
all_birds.append(bird_5)


artiodactyl_1 = Chordate('корова', 'Манька', 'мычание')
artiodactyl_1.weight = 50
artiodactyl_1.feed()
artiodactyl_1.milking()
all_animals.append(artiodactyl_1)

artiodactyl_2 = Chordate('коза', 'Рога', 'блеяние')
artiodactyl_2.weight = 35
artiodactyl_2.feed()
artiodactyl_2.milking()
all_animals.append(artiodactyl_2)

artiodactyl_3 = Chordate('коза', 'Копыта', 'блеяние')
artiodactyl_3.weight = 30
artiodactyl_3.feed()
artiodactyl_3.milking()
all_animals.append(artiodactyl_3)

artiodactyl_4 = Chordate('овца', 'Барашек', 'блеяние')
artiodactyl_4.weight = 50
artiodactyl_4.feed()
artiodactyl_3.shearing()
all_animals.append(artiodactyl_4)

artiodactyl_5 = Chordate('овца', 'Кудрявый', 'блеяние')
artiodactyl_5.weight = 55
artiodactyl_5.feed()
artiodactyl_5.shearing()
all_animals.append(artiodactyl_5)


total_weight, heaviest_creature = weight_count(all_birds)
print('Общий вес птиц: ' + str(total_weight) + '\nСамое тяжелый: ' + heaviest_creature)

total_weight, heaviest_creature = weight_count(all_animals)
print('Общий вес животных: ' + str(total_weight) + '\nСамое тяжелый: ' + heaviest_creature)

full_list = all_animals + all_birds
test = Animals()
test.feed(full_list)


