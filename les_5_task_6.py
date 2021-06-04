import re


def calc_hours(calc_line: str):
    line_of_hours = re.sub(r'\D', ' ', calc_line)
    total_hours = 0
    for hour in line_of_hours.split():
        total_hours += float(hour)
    return total_hours


dictionary = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        line = i.split(':')
        dictionary[line[0]] = calc_hours(line[1])
print(f'{dictionary}')