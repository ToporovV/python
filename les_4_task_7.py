from math import factorial
from itertools import count

numbers = input('Введите диапазон чисел через пробел: ').split()
numbers = [int(i) for i in numbers]
start = numbers[0]
stop = numbers[1]


def fibo_gen():
    for i in range(start, stop + 1):
        yield factorial(i)


for i in fibo_gen():
    print(i)
        #n += 1
    #else:
        #break
