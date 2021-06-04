class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_number(e):
    try:
        float(e)
        return True
    except ValueError:
        return False


result_list = []
while True:

    numbers = input('Введите число для заполнения списка, для выхода на жмите "q": ')
    if numbers == 'q':
        break

    try:
        if not (is_number(numbers)):
            raise OwnError('Введите число!')
    except OwnError as err:
        print(err)
    else:
        numbers = int(numbers)
        result_list.append(numbers)

print(result_list)
