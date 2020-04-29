with open('text_1.txt', 'w', encoding='utf-8') as file:
    while True:
        string = input('Введите слово: ')

        if not string:
            print('Выход')
            break

        file.write(f'{string}\n')
