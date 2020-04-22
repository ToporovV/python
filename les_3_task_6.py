def int_func(text):
    return text.title()


my_list = []
words = input('Введите несколько слов через пробел: ').split(' ')
print(words)
for i in words:
    my_list.append(int_func(i))
result = ' '.join(my_list)
print(f'Строка получилась: {result}')

