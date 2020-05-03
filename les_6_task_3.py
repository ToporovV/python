class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}\nДолжность: {self.position}')

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Виктор', 'Лучин', 'инженер', 20000, 16000)
position.get_full_name()
print(f'Доход с учетом премии составляет: {position.get_total_income()} руб.')
