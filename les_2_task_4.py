user_enter = input('Введите несколько слов разделенных пробелами: ').split()
for i, items in enumerate(user_enter, 1):
    print(f'{i}) {items.title():.10s}')