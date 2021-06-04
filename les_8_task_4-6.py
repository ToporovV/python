class Warehouse:
    def __init__(self):
        self.total = 0
        self.unit_warehouse = {}
        self.unit_accounting = {}
        self.unit_office = {}
        self.unit_hr = {}
        self.questions_template = (
            {'Наименование': 'Введите наименование товара: '},
            {'Цена': 'Введите цену товара: '},
            {'Количество': 'Введите количество товара: '}
        )

    @staticmethod
    def is_int(number: str):
        try:
            int(number)
            return True
        except:
            return False

    def reception(self):
        user_input = input('Для начала ввода товара нажмите "Enter", для выхода нажмите "q": ')
        while user_input != 'q':
            user_dict = {}
            for i in self.questions_template:
                key = tuple(i)[0]
                tmp = input(i[key])
                if key == 'Цена':
                    if self.is_int(tmp):
                        tmp = int(tmp)
                    else:
                        print('Неверный тип данных! Введите число.')
                        return
                elif key == 'Количество':
                    if self.is_int(tmp):
                        tmp = int(tmp)
                        self.total += tmp
                    else:
                        print('Неверный тип данных! Введите число.')

                user_dict.update({key: tmp})

            try:
                user_input = int(input('Введите код подразделения (1-Склад/2-Бухгалтерия/3-Офис/4-Отдел кадров): '))
            except ValueError:
                print('Код должен состоять из чисел!')

            if user_input == 1:
                user_input = 'Склад'
                self.unit_warehouse.update({user_input: user_dict})
            elif user_input == 2:
                user_input = 'Бухгалтерия'
                self.unit_accounting.update({user_input: user_dict})
            elif user_input == 3:
                user_input = 'Офис'
                self.unit_office.update({user_input: user_dict})
            elif user_input == 4:
                user_input = 'Отдел кадров'
                self.unit_hr.update({user_input: user_dict})

            user_input = input('Для продолжения нажмите "Enter", для выхода нажмите "q": ')


class OfficeEquipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name: str, price: int, print: str):
        super().__init__(name, price)
        self.print = print


class Scanner(OfficeEquipment):
    def __init__(self, name: str, price: int, scan: str):
        super().__init__(name, price)
        self.scan = scan


class Xerox(OfficeEquipment):
    def __init__(self, name: str, price: int, copy: str):
        super().__init__(name, price)
        self.copy = copy


w = Warehouse()
w.reception()
print(w.unit_warehouse)
print(w.unit_accounting)
print(w.unit_office)
print(w.unit_hr)
print(f'Общее количесво техники: {w.total} шт.')
