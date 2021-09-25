""" Transport class """
from abc import ABC, abstractmethod

class Transport(ABC):
    """Transport class"""
    def __init__(self, *args, **kwargs):
        self.brand = kwargs.get('transport_type', 'DefType')
        self.model = kwargs.get('model', 'DefModel')
        self.engine_type = kwargs.get('engine_type', 'DefEngine')
        self.seats = kwargs.get('seats', 1)
        self.passengers = 0
        self.engine_status = 'OFF'

    @abstractmethod
    def add_passenger(self, passenger):
        """Добавить пассажиров"""
        raise NotImplementedError('Необходимо переопределить метод')

    @abstractmethod
    def engine(self):
        """Включить/выключить двгатель"""
        raise NotImplementedError('Необходимо переопределить метод')
