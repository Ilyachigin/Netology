
def recipes_list(lines):
    new_list = []
    for line in lines:
        new_list.append(line.replace('\n', ''))
    for find in new_list:
        if find == '':
                new_list.remove(find)
    return new_list


def find_ingridients(new_list):
    new_book = []
    for find in new_list:
        name = new_list.pop(0)
        quantity = new_list.pop(0)
        ingridients = []
        for thing in range(int(quantity)):
            ingridients.append(new_list[thing])
        for delete in ingridients:
            new_list.remove(delete)
        new_book.append({name: ingridients})
    return new_book


def cook_dictianary(new_book):
    for all in range(len(new_book)):
        for key, values in new_book[all].items():
            dishes_list = []
            for things in values:
                split_things = things.split('|')
                dishes_dict = {"ingredient_name": split_things[0].strip(),
                               "quantity": split_things[1].strip(),
                               "measure": split_things[2].strip() + '.'}
                dishes_list.append(dishes_dict)
            new_book[all][key] = dishes_list
    return new_book


def cookbook(lines):
    cook_book = {}
    cook_list = recipes_list(lines)
    ingridients_book = find_ingridients(cook_list)
    new_book = cook_dictianary(ingridients_book)
    for cook in new_book:
        cook_book.update(cook)
    return cook_book


def read_recipes():
    with open('recipes.txt', 'r') as file:
        lines = file.readlines()
    return lines


def get_shop_list_by_dishes(dishes, person_count=None):
    shop_list = {}
    lines = read_recipes()
    recipes = cookbook(lines)
    recipes_list = []
    for recipe in recipes:
        recipes_list.append(recipe)
    for dish in dishes:
        if dish not in recipes_list:
            print(dish + ' нет в книге рецептов.')
        else:
            for recipe in recipes:
                if dish == recipe:
                    for part in recipes[recipe]:
                        if person_count:
                            quantity = int(list(part.items())[1][1]) * person_count
                        else:
                            quantity = int(list(part.items())[1][1])
                        if part['ingredient_name'] in shop_list.keys():
                            shop_list[part['ingredient_name']]['quantity'] += quantity
                        else:
                            ingredients_list = {
                                part['ingredient_name']: {list(part.items())[2][0]: list(part.items())[2][1],
                                                          list(part.items())[1][0]: quantity}}
                            shop_list.update(ingredients_list)
    return shop_list


# Task #1
lines = read_recipes()
book = recipes_list(lines)
print(book)

# Task #2
shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
print(shop_list)

