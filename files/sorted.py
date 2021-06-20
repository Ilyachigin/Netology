
def read_text():
    with open('notes/1.txt', 'r') as file:
        first_lines = file.readlines()
    with open('notes/2.txt', 'r') as file:
        second_lines = file.readlines()
    with open('notes/3.txt', 'r') as file:
        third_lines = file.readlines()
    return first_lines, second_lines, third_lines


def write_text(sorted_list):
    with open('notes/sorted.txt', 'w') as file:
        file.write('\n'.join(sorted_list))


def sorting():
    len_list = []
    lines_list = []
    sorted_list = []
    first_lines, second_lines, third_lines = read_text()
    lines_list.append(first_lines)
    lines_list.append(second_lines)
    lines_list.append(third_lines)
    for line in lines_list:
        len_list.append(len(line))
    sort = False
    while not sort:
        for lines in lines_list:
            if not len_list:
                sort = True
                break
            else:
                longest = max(len_list)
                if longest == len(lines):
                    if first_lines == lines:
                        name = '1.txt'
                        new_line = lines
                        len_list.remove(longest)
                    elif second_lines == lines:
                        name = '2.txt'
                        new_line = lines
                        len_list.remove(longest)
                    else:
                        name = '3.txt'
                        new_line = lines
                        len_list.remove(longest)
                    sorted_list.append(name)
                    sorted_list.append(str(len(new_line)))
                    for line in new_line:
                        sorted_list.append(str(line).replace("\n", ""))
    final_list = []
    for sort in sorted_list:
        final_list.append(sort)
    return final_list


sorted_list = sorting()
write_text(sorted_list)

