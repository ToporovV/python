class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return f'Результат операции сложения: {self.quantity + other.quantity}'

    def __sub__(self, other):
        return f'Результат операции вычитания: {self.quantity - other.quantity}' if (self.quantity - other.quantity) > 0 else print(
            'Результат отрицательный.')

    def __mul__(self, other):
        return f'Результат операции умножения: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Результат операции деления: {round(self.quantity / other.quantity)}'

    def make_order(self, cells_in_number):
        number = ''
        for i in range(self.quantity // cells_in_number):
            number += f'{"*" * cells_in_number}\n'
        number += f'{"*" * (self.quantity % cells_in_number)}'
        return number


cell_1 = Cell(15)
cell_2 = Cell(4)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(3))