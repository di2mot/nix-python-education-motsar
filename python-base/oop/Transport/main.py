""" Python - OOP - 1 @Dima Motsar"""

from transport import Transport
from animal import Animal
from fly import Fly


class Hatchback(Transport):
    """Хэтчбег"""
    def __init__(self, transport_type, model, engine_type, seats):
        Transport.__init__(self, transport_type, model, engine_type, seats)

    def add_passenger(self, passenger: int):
        """Добавить пассажиров"""
        if self.passengers + passenger <= self.seats:
            self.passengers += passenger
            sets_left = self.seats - self.passengers
            print(f'Мест осталось: {sets_left}')
        else:
            print('Мест больше нет')


    def engine(self):
        if self.engine_status == 'OFF':
            self.engine_status = 'ON'

        else:
            self.engine_status = 'OFF'
        return f"Engine is {self.engine_status}"


class Wagon(Transport, Animal):
    """Гужевая повозка"""
    def __init__(self, transport_type, model, engine_type, seats, *args, **kwargs):
        Transport.__init__(self, transport_type, model, engine_type, seats)
        Animal.__init__(self, *args, **kwargs)
        self.kind = kwargs.get('kind', 'DefKind')
        self.name = kwargs.get('name', 'DefName')
        self.drink_passengers = False
        self.hunger = False
        self.power = 100


    def add_passenger(self, passenger: int):
        if self.passengers + passenger <= self.seats:
            self.passengers += passenger
            sets_left = self.seats - self.passengers
            print(f'Мест осталось: {sets_left}')
        elif self.drink_passengers:
            self.passengers += passenger
        else:
            delete_passengers = self.seats - self.passengers + passenger
            print(f'Выпало паасажиров: {delete_passengers}')

    def sleep(self, day_time):
        if 22 < day_time > 6:
            print(f'{self.kind} по имени {self.name} уже спит')
        else:
            print(f'{self.kind} по имени {self.name} работает')


    def engine(self):
        if self.engine_status == 'OFF' and not self.hunger:
            self.engine_status = 'ON'
        else:
            self.engine_status = 'OFF'
        return f"Engine is {self.engine_status}"

    @property
    def get_passengers(self):
        """Количество пассажиров"""
        return self.passengers

    def get_power(self, food):
        """Запрвка"""
        self.power += food

class Pickup(Transport):
    """Пикап"""
    def __init__(self, *args, **kwargs):
        Transport.__init__(self, *args, **kwargs)
        self.max_cargo = kwargs.get('cargo', 0)
        self.total_cargo = 0
        print(self.max_cargo)

    def add_passenger(self, passenger):
        passenger_n, weight = passenger
        if self.passengers + passenger_n <= self.seats and self.add_cargo(weight):
            self.passengers += passenger_n
            sets_left = self.seats - self.passengers
            print(f'Мест осталось: {sets_left}')
        else:
            print('Мест больше нет')


    def engine(self):
        if self.engine_status == 'OFF':
            self.engine_status = 'ON'

        else:
            self.engine_status = 'OFF'
        return f"Engine is {self.engine_status}"

    def add_cargo(self, item):
        """ Добавить груз """
        if self.max_cargo >= self.total_cargo + item:
            self.total_cargo += item
            res = True
            print(f'Добавленно {item} кг')
        else:
            print(f'Слишком ного весит. Свободно {self.free_space}')
            res = False
        return res

    @property
    def free_space(self):
        """Расчёт свободного места"""
        return self.max_cargo - self.total_cargo


class Bird(Animal, Fly):
    """ Модеаль Альбатроса """
    def __init__(self, *args, **kwargs):
        Animal.__init__(self, *args, **kwargs)
        Fly.__init__(self, *args, **kwargs)
        self.wings = kwargs.get('wings', 0)
        self.length = kwargs.get('length', 1)
        self.area = self.area_calc()
        self.speed = kwargs.get('speed', 1)
        self.weight = kwargs.get('weight', 1)
        self.lift_force = self.lifting_force((self.area, self.speed, self.weight))
        self.power = 100



    def area_calc(self):
        """расчёт площади"""
        return self.wings * self.length

    @staticmethod
    def lifting_force(kwargs: tuple):
        """ РСчёт подъёмной силы
         co: коэфициент подъёмной силы
         qo: массовая плотность воздуха
         """
        area, speed, weight = kwargs
        coof_lift = 28
        air_density = 1.25
        lift_force = coof_lift * ((air_density * speed ** 2) / 2) * area
        return lift_force // weight

    def sleep(self, day_time):
        """ Хочет ли животное спать """
        if 22 > day_time > 6:
            print(f'{self.kind} по имени {self.name} уже спит')
        else:
            print(f'{self.kind} по имени {self.name} работает')

    def muve(self):
        """ Двигает ли оно """
        if self.hunger:
            msg = False
        else:
            msg = True
        return msg

    def get_power(self, food):
        """Запрвка"""
        self.power += food

class Plain(Transport, Fly):
    """Базовый класс самолёта"""
    def __init__(self, *args, **kwargs):
        Transport.__init__(self, *args, **kwargs)
        Fly.__init__(self, *args, **kwargs)
        self.weight = kwargs.get('weight', 100)
        self.max_cargo = kwargs.get('cargo', 100)
        self.total_cargo = kwargs.get('total_cargo', 0)
        self.free_space = kwargs.get('max_cargo', 100)

    def area_calc(self):
        """Расчёт площади"""
        return self.wings * self.length

    def add_passenger(self, passenger: int, **kwargs):
        weight = kwargs.get('weight', 1)
        if self.passengers + passenger <= self.seats and self.add_cargo(weight):
            self.passengers += passenger
            sets_left = self.seats - self.passengers
            print(f'Мест осталось: {sets_left}')
        else:
            print('Мест больше нет')


    def engine(self):
        if self.engine_status == 'OFF':
            self.engine_status = 'ON'

        else:
            self.engine_status = 'OFF'
        return f"Engine is {self.engine_status}"

    def add_cargo(self, item):
        """Добавить груз"""
        if self.max_cargo >= self.total_cargo + item:
            self.total_cargo += item
            res = True
            print(f'Добавленно {item} кг')
        else:
            print(f'Слишком ного весит. Свободно {self.free_space}')
            res = False
        return res


    def lifting_force(self, kwargs=0):
        """ РСчёт подъёмной силы
         coof_lift: коэфициент подъёмной силы
         air_density: массовая плотность воздуха
         """
        area = self.area_calc()
        coof_lift = 28
        air_density = 1.25
        lift_force = coof_lift * ((air_density * self.speed ** 2) / 2) * area
        res = (lift_force // self.weight)
        return res

    def get_power(self, fuel):
        """Запрвка"""
        self.fuel += fuel


car_1  = Hatchback('Tayota', 'camry', 'v6', 6)
car_1.add_passenger(1)
car_1.add_passenger(2)
print(car_1.engine)


village_car = Wagon('Povozka', 'Flash', 'v1', 6, ('Horse', 'Boorka'))
print(village_car.name)
print(village_car.sleep(10))
print(village_car.get_passengers)

pirat = Bird('Albatros', 'Pirat', 'wings', 3.2, 0.1, 30, 11)
print(f'Подъёмная сила {pirat.kind} {pirat.lift_force} H')

chack_noris_car = Pickup(transport_type='Ford', model='F500', engine_type='v6', seats=4, cargo=500)
chack_noris_car.add_cargo(10)

plain = Plain(transport_type='plain', model='A320neo', engine_type='LEAPВ',
              total_cargo=250, wings=35.8, length=44, cargo=780, free_space=100)
print(f'Подъёмная сила {plain.model} {plain.lifting_force()} H')
