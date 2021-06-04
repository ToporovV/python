dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
            }

with open('text_4.txt', 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open('text_4_1.txt', 'w', encoding='utf-8') as file_write:
    for i in lines:
        line = i.split()
        line[0] = dictionary[line[0]]
        print(' '.join(line), file=file_write)
