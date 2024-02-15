# if __name__ == "__main__":
#     # Write your solution here
#     pass

from typing import Optional


class Vehicle:
    """Базовый класс Транспортное средство."""

    def __init__(self, make: str, model: str, year: int):
        self.make = make  # Марка
        self.model = model  # Модель
        self.year = year  # Год выпуска

    def drive(self, destination: str) -> None:
        """Направиться к указанному месту."""
        pass

    def stop(self) -> None:
        """Остановиться."""
        pass

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        pass

    def __repr__(self) -> str:
        """Возвращает представление объекта для интерпретатора."""
        pass


class Car(Vehicle):
    """Дочерний класс Автомобиль, наследует от класса Vehicle."""

    def __init__(self, make: str, model: str, year: int, fuel_type: str, passengers: Optional[int] = 4):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type  # Тип топлива
        self.passengers = passengers  # Количество пассажиров

    def drive(self, destination: str) -> None:
        """Направиться к указанному месту на автомобиле."""
        pass

    def park(self) -> None:
        """Припарковать автомобиль."""
        pass

    def __repr__(self) -> str:
        """Возвращает представление объекта для интерпретатора."""
        pass

    def stop(self) -> None:
        """Остановить автомобиль."""
        pass


class Truck(Vehicle):
    """Дочерний класс Грузовик, наследует от класса Vehicle."""

    def __init__(self, make: str, model: str, year: int, payload_capacity: float):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity  # Грузоподъемность (в тоннах)

    def load_cargo(self, cargo: str, weight: float) -> None:
        """Загрузить груз в грузовик."""
        pass

    def unload_cargo(self, cargo: str) -> None:
        """Выгрузить груз из грузовика."""
        pass

    def __repr__(self) -> str:
        """Возвращает представление объекта для интерпретатора."""
        pass

    def drive(self, destination: str) -> None:
        """Направиться к указанному месту на грузовике."""
        pass


if __name__ == "__main__":
    # Создание экземпляра автомобиля
    car = Car(make="Toyota", model="Camry", year=2022, fuel_type="Бензин", passengers=4)

    # Создание экземпляра грузовика
    truck = Truck(make="Volvo", model="FH16", year=2020, payload_capacity=20.5)

    # Пример использования методов
    print("Автомобиль:")
    print(car)
    car.drive("гипермаркет")
    car.stop()
    car.park()

    print("\nГрузовик:")
    print(truck)
    truck.drive("склад")
    truck.load_cargo("Ящики", 15.2)
    truck.unload_cargo("Ящики")
