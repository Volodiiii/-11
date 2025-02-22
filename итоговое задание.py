from abc import ABC, abstractmethod


class Appliance(ABC):
    """
    Базовый класс для бытовой техники.
    """

    def __init__(self, brand: str, model: str, power: int) -> None:
        """
        Инициализация базовых атрибутов.
        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param power: Потребляемая мощность (Вт).
        """
        self._brand = brand  # Инкапсуляция, так как бренд редко меняется
        self._model = model  # Инкапсуляция, так как модель не изменяется после создания
        self.power = power

    def __str__(self) -> str:
        return f"{self._brand} {self._model} (Мощность: {self.power} Вт)"

    def __repr__(self) -> str:
        return f"Appliance(brand={self._brand}, model={self._model}, power={self.power})"

    @abstractmethod
    def turn_on(self) -> None:
        """
        Абстрактный метод для включения устройства.
        """
        pass


class Refrigerator(Appliance):
    """
    Дочерний класс для холодильников.
    """

    def __init__(self, brand: str, model: str, power: int, temperature: float) -> None:
        """
        Инициализация холодильника с дополнительным параметром - температурой.
        :param temperature: Температура в холодильной камере.
        """
        super().__init__(brand, model, power)
        self.temperature = temperature

    def turn_on(self) -> None:
        """
        Реализация метода включения холодильника.
        """
        print(f"{self._brand} {self._model} включен. Температура: {self.temperature}°C")

    def __str__(self) -> str:
        return f"{super().__str__()}, Температура: {self.temperature}°C"

    def adjust_temperature(self, new_temp: float) -> None:
        """
        Перегруженный метод для настройки температуры холодильника.
        Причина перегрузки: у холодильников есть уникальная возможность изменять температуру.
        :param new_temp: Новая температура.
        """
        self.temperature = new_temp
        print(f"Температура установлена на {self.temperature}°C")


class WashingMachine(Appliance):
    """
    Дочерний класс для стиральных машин.
    """

    def __init__(self, brand: str, model: str, power: int, drum_capacity: float) -> None:
        """
        Инициализация стиральной машины с дополнительным параметром - вместимость барабана.
        :param drum_capacity: Вместимость барабана в кг.
        """
        super().__init__(brand, model, power)
        self.drum_capacity = drum_capacity

    def turn_on(self) -> None:
        """
        Реализация метода включения стиральной машины.
        """
        print(f"{self._brand} {self._model} включена. Вместимость: {self.drum_capacity} кг")

    def __str__(self) -> str:
        return f"{super().__str__()}, Вместимость: {self.drum_capacity} кг"

    def start_wash_cycle(self, mode: str) -> None:
        """
        Перегруженный метод для запуска стирки.
        Причина перегрузки: стиральные машины имеют различные режимы стирки.
        :param mode: Режим стирки.
        """
        print(f"Старт цикла стирки в режиме: {mode}")


# Пример использования
fridge = Refrigerator("LG", "GR-389SQF", 150, 4.0)
washing_machine = WashingMachine("Samsung", "WW90T", 2000, 9.0)

print(fridge)
fridge.turn_on()
fridge.adjust_temperature(2.0)

print(washing_machine)
washing_machine.turn_on()
washing_machine.start_wash_cycle("Деликатный")