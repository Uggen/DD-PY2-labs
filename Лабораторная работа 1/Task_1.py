# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    """Car"""
    def __init__(self, speed: int, body: str, brand: str):
        """
        Создание и подготовка к работе объекта Машины.

        :param speed: Скорость машины.
        :param body: Кузов машины.
        :param brand: Марка машины.
        """
        self.speed = speed
        self.body = body
        self.bran = brand

    def going(self) -> int:
        """
        Функция, которая осуществляет движение машины.

        :result:

        >>> car_1 = Car(0, "Джип", "Audi")
        >>> car_1.going()
        """
        ...

    def turn(self) -> bool:
        """
        Функция, которая выполняет поворот автомобиля.

        :result:

        >>> car_1 = Car(0, "Джип", "Audi")
        >>> car_1.turn()
        """
        ...

    def stop(self) -> bool:
        """
        Функция, которая проверяет, остановилась ли машина на красный свет светофора.

        :result:

        >>> car_1 = Car(0, "Джип", "Audi")
        >>> car_1.stop()
        """
        ...


class TrafficLightFoCar:
    """Светофор"""
    def __init__(self, green: bool, yellow: bool, red: bool):
        """
        Сигнал светофора.

        :param green: Зеленый сигнал.
        :param yellow: Желтый сигнал.
        :param red: Красный сигнал.
        """
        self.green = green
        self.yellow = yellow
        self.red = red

    def switch_the_color(self) -> bool:
        """
        Функция, которая меняет сигнала светофора.
        :result: Сигнал светофора изменен на {signal}.

        >>> light_1 = TrafficLightFoCar(False, False, True)
        >>> light_1.switch_the_color()
        """
        ...

    def repair_mod(self) -> bool:
        """
        Функция, которая проверят, сломан ли светофор.
        :result: Светофор исправен или сломан.

        >>> light_1 = TrafficLightFoCar(False, False, True)
        >>> light_1.repair_mod()
        """
        ...


class TrafficLightFoPeople:
    """Светофор"""
    def __init__(self, green: bool, yellow: bool, red: bool):
        """
        Сигнал светофора.

        :param green: Зеленый сигнал.
        :param yellow: Желтый сигнал.
        :param red: Красный сигнал.
        """
        self.green = green
        self.yellow = yellow
        self.red = red

    def switch_the_color(self) -> bool:
        """
        Функция, которая меняет сигнала светофора.

        :result:

        >>> light_2 = TrafficLightFoPeople(True, False, False)
        >>> light_2.switch_the_color()
        """
        ...

    def repair_mod(self) -> bool:
        """
        Функция, которая проверят, сломан ли светофор.

        :result:

        >>> light_2 = TrafficLightFoPeople(True, False, False)
        >>> light_2.repair_mod()
        """
        ...


class People:
    """Пешеход"""
    def __init__(self, speed: int, state: bool):
        """
        Объект пешехода.
        :param speed: Скорость пешехода.
        :param state: Состояние пешехода стоит он или нет.
        """
        self.speed = speed
        self.state = state

    def cross_the_road(self) -> bool:
        """
        Функция, которая проверяет пешеходит ли дорогу пешеход

        :result:

        >>> people_1 = People(20, True)
        >>> people_1.cross_the_road()
        """
        ...

    def stop(self) -> bool:
        """
        Функция, которая проверяет, стоит ли пешеход на красный сигнал светофора.

        :result:

        >>> people_1 = People(20, True)
        >>> people_1.stop()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    # car = Car(0, "Джип", "Audi")
    # traffic_light_1 = TrafficLightFoCar(False, False, True)
    # traffic_light_2 = TrafficLightFoPeople(True, False, False)
    # people = People(20, True)
    #
    # print(traffic_light_1.switch_the_color())
    # print(traffic_light_2.switch_the_color())
    # print(people.stop())
    # print(car.going())

    import doctest

    doctest.testmod()

