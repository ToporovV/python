class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - self.b * other.b} + {self.b + other.a + self.a + other.b} * i'


z_1 = ComplexNumbers(1, 2)
z_2 = ComplexNumbers(3, 8)
print(z_1 + z_2)
print(z_1 * z_2)