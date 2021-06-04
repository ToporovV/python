from abc import ABC, abstractmethod


class Dress(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def square(self):
        pass

    def __str__(self):
        return f'Площадь ткани требуемая для {self.name}: {self.square}'

    def __add__(self, other):
        return f'Общая площадь ткани: {self.square + other.square}'


class Coat(Dress):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def square(self):
        return round((self.size / 6.5 + 0.5), 2)


class Costume(Dress):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def square(self):
        return round((2 * self.height + 0.3), 2)


coat = Coat('пальто', 50)
costume = Costume('костюм', 180)
print(coat)
print(costume)
print(costume + coat)
