class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(self.title)


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(self.title)


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print(self.title)


s = Stationery()
p = Pen()
pc = Pencil()
h = Handle()

s.draw()
p.draw()
pc.draw()
h.draw()