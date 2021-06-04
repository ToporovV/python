# Решение через dict
seasons = {'зима': (1, 2, 12),
           'весна': (3, 4, 5),
           'лето': (6, 7, 8),
           'осень': (9, 10, 11)}

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(f'Время года: {key.title()}')

# Решение через list
months = ['зима', 'весна', 'лето', 'осень']

month_number = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month_number >= 1 and month_number <= 2 or month_number == 12:
    print(f'Время года: {months[0].title()}')
elif month_number >= 3 and month_number <=5:
    print(f'Время года: {months[1].title()}')
elif month_number >= 6 and month_number <= 8:
    print(f'Время года: {months[2].title()}')
else:
    print(f'Время года: {months[3].title()}')