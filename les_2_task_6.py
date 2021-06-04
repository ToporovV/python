products = []
i = 1
while True:
    products.append(
        (int(input('Введите номер товара: ')), dict({
            'название': input('Введите название товара: '),
            'цена': int(input('Введите цену товара: ')),
            'количество': int(input('Введите количество товара: ')),
            'eд': input('Введите единцы измерения: '),
        }))
    )
    ex = input('Вы хотите добавить еще один товар? (да/нет): ')
    if ex == 'нет':
        break
    i += 1
print(f'Список: {products}')

analytics = dict({})
for product in products:
    for key, value in product[-1].items():
        if key in analytics:
            if value not in analytics.get(key):
                analytics.get(key).append(value)
        else:
            analytics.update({key: [value]})

print(f'Аналитика: {analytics}')