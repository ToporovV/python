with open('text_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'В файле {len(lines)} строк(и).')

    for i, line in enumerate(lines, 1):
        print(f'В строке {i} {len(line.split())} слов.')
