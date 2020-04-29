with open('text_3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    result = 0
    count = 0
    for i in lines:
        line = i.split()
        if float(line[1]) < 20000:
            print(f'Сотрудник {line[0]} имеет оклад менее 20000 руб')
        result += float(line[1])
        count += 1
        total = result / count
    print(F'Средняя зарплата сотрудников {round(total, 1)} руб')

