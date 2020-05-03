import time


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


class TrafficLight:
    __color = None

    def running(self):
        self.__color = u"\u2588"
        print(f'{bcolors.RED}{self.__color}{bcolors.END}')
        time.sleep(7)

        self.__color = u"\u2588"
        print(f'{bcolors.YELLOW}{self.__color}{bcolors.END}')
        time.sleep(2)

        self.__color = u"\u2588"
        print(f'{bcolors.GREEN}{self.__color}{bcolors.END}')
        time.sleep(7)

        self.__color = u"\u2588"
        print(f'{bcolors.YELLOW}{self.__color}{bcolors.END}')
        time.sleep(2)

        while True:
            self.running()


TrafficLight = TrafficLight()
TrafficLight.running()
