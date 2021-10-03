"""Animal class """
from abc import ABC, abstractmethod

class Animal(ABC):
    """Базовый абстрактный клас животного"""
    def __init__(self, *args, **kwargs):
        self.kind = kwargs.get('kind', 'kind')
        self.name = kwargs.get('name', 'name')
        self.feet = 4
        self.hunger = False
        self.speed = 0
        self.animal_weihgt = 0
        self.power = 100

    @abstractmethod
    def sleep(self, day_time):
        """ Животное должно спать """
        raise NotImplementedError('Необходимо переопределить метод')

    @abstractmethod
    def get_power(self, food):
        """Запрвка"""
        self.power += food
