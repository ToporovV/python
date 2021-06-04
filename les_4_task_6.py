from itertools import count, cycle

start = int(input('Введите стартовое число: '))
stop = int(input('Введите конечное число: '))
for i in count(start):
    if i > stop:
        break
    else:
        print(i)

print('*' * 50)

my_list = [1122, 'ABC', True]

n = 0
for i in cycle(my_list):
    if n > 20:
        break
    print(i)
    n += 1
