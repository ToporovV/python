user_number = int(input('Введите целое положительное число: '))
max_elem = 0

while user_number != 0:
    elem = user_number % 10
    user_number = user_number // 10
    if elem > max_elem:
        max_elem = elem

print(f'Самая большая цифра в числе: {max_elem}')
