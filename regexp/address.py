import re
import csv

pattern = r'^(\+7|8)?\s?\(?(\d{3})\)?\s?\-?(\d{3})(\-?(\d{2}))?(\-?(\d{2}))?\s?\(?([а-я]+)?\.?\s?(\d{4})?\)?'
sub = r'+7(\2)\3-\5-\7'

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

items = {}
for contact in contacts_list[1:]:
    fio = ' '.join(contact[:3])
    if len(fio.split()) == 2:
        contact[:2] = fio.split()
    else:
        contact[:3] = fio.split()
    contact[5] = re.sub(pattern, sub, contact[5])
    item = items.get((contact[0], contact[1]), {})
    for num, val in enumerate(contact):
        if item.get(num, '') == '':
            item[num] = val
    items[(contact[0], contact[1])] = item
contacts = [list(item.values()) for item in items.values()]
contacts_list = contacts_list[:1] + contacts


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
