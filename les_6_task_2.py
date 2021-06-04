class Road:
    __length = None
    __width = None
    __weight = 25
    __cover = 5

    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def calculate(self):
        result = (self.__length * self.__width * self.__weight * self.__cover) / 1000
        print(f'Для покрытия всего дорожного полотна необходимо {result} тонн.')


Road(2000, 10).calculate()
