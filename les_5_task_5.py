from random import randint

with open('text_5.txt', 'w', encoding='utf-8') as file_write:
    numbers = [str(randint(10, 100)) for i in range(20)]
    print(' '.join(numbers), file=file_write)

with open('text_5.txt', 'r', encoding='utf-8') as file_read:
    num = file_read.readline().split()
    num_sum = 0
    for i in num:
        num_sum += int(i)

print(f'Сумма всех чисел: {num_sum}')
