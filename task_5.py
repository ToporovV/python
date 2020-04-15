revenue = int(input('Введите значение выручки вашей фирмы в рублях: '))
costs = int(input('Введите значение издержек вашей фирмы в рублях: '))

if revenue > costs:
    result = revenue - costs
    profit = result / revenue
    print(f'Фирма работает с прибылью {result} руб. Рентабельность выручки составляет {profit}.')
    number_of_staff = int(input('Введите количество сотрудников в вашей фирме: '))
    result_number = result / number_of_staff
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет {result_number} руб/чел.')
elif revenue < costs:
    result = revenue - costs
    print(f'Фирма работает в убыток {result} руб.')
else:
    print(f'Фирма работает в ноль.')
