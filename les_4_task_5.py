from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


my_list = [i for i in range(1, 11) if i % 2 == 0]  # аналогично диапазон range(100, 1001), но так проще проверить
print(my_list)

result = reduce(my_func, my_list)
print(result)
