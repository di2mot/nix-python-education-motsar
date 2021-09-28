from abc import ABC, abstractmethod

class Water(ABC):
    """Базовый класс полёта"""
    def __init__(self, *args, **kwargs):
        """
        lift: подъёмная сила
        """
        self.engine_type = kwargs.get('engine_type', 'gas')
        self.speed = kwargs.get('speed', 1)
        self.length = kwargs.get('length', 1)
        self.wings = kwargs.get('wings', 1)
        self.height = kwargs.get('height', 1)
        self.fuel = 100

    @abstractmethod
    def displacement(self):
        """Расчёт водоизмещения"""
        raise NotImplementedError('Необходимо переопределить метод')

    @abstractmethod
    def get_power(self, fuel):
        """Запрвка"""
        raise NotImplementedError('Необходимо переопределить метод')