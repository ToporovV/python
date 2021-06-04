class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self, speed):
        print(f'Текущая скорость {speed} км/ч.')


class TownCar(Car):

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def show(self):
        if self.is_police != True:
            self.is_police = 'Нет'
        print(
            f'Марка машины: {self.name}\nЦвет машины: {self.color}\nПолицейская машина: {self.is_police}')

    def show_speed(self, speed):
        if speed > 60:
            print('Превышение разрешенной скорости в 60 км/ч.')
        else:
            print(f'Текущая скорость {speed} км/ч.')


class SportCar(Car):
    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def show(self):
        if self.is_police != True:
            self.is_police = 'Нет'
        print(
            f'Марка машины: {self.name}\nЦвет машины: {self.color}\nПолицейская машина: {self.is_police}')


class WorkCar(Car):
    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def show(self):
        if self.is_police != True:
            self.is_police = 'Нет'
        else:
            self.is_police = 'Да'
        print(
            f'Марка машины: {self.name}\nЦвет машины: {self.color}\nПолицейская машина: {self.is_police}')

    def show_speed(self, speed):
        if speed > 40:
            print('Превышение разрешенной скорости в 40 км/ч.')
        else:
            print(f'Текущая скорость {speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def show(self):
        if self.is_police != True:
            self.is_police = 'Нет'
        else:
            self.is_police = 'Да'
        print(
            f'Марка машины: {self.name}\nЦвет машины: {self.color}\nПолицейская машина: {self.is_police}')


tc = TownCar('Volvo', 'Белый', False)
tc.show()
tc.show_speed(70)
tc.go()
tc.stop()
tc.turn('направо')

sc = SportCar('Ferrari', 'Красный', False)
sc.show()
sc.show_speed(100)
sc.go()
sc.stop()
sc.turn('налево')

wc = WorkCar('KAMAZ', 'Оранжевый', False)
wc.show()
wc.show_speed(60)
wc.go()
wc.stop()
wc.turn('назад')

pc = PoliceCar('FORD', 'Бело-синий', True)
pc.show()
pc.show_speed(90)
pc.go()
pc.stop()
pc.turn('назад')
