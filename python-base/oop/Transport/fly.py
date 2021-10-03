""" Базовый воздушый класс """
from abc import ABC, abstractmethod

class Fly(ABC):
    """Базовый класс полёта"""
    def __init__(self, *args, **kwargs):
        """
        lift: подъёмная сила
        """
        self.engine_type = kwargs.get('engine_type', 'gas')
        self.air_density = 0
        self.length = kwargs.get('length', 1)
        self.speed = kwargs.get('speed', 1)
        self.wings = kwargs.get('wings', 1)
        self.fuel = 100

    @abstractmethod
    def lifting_force(self, **kwargs):
        """Добавить пассажиров"""
        raise NotImplementedError('Необходимо переопределить метод')

    @abstractmethod
    def get_power(self, fuel):
        """Запрвка"""
        self.fuel += fuel
