import datetime
from enum import Enum


class FoodTemperature(Enum):
    is_cold = True
    is_warm = False
    is_hot = True


class Door(Enum):
    is_closed = True

    def __init__(self, val):
        # No need to set self.name. It's already handled.
        self.val = val

    # def __setattr__(self, key, value):
    #     self.value = value


class Light(Enum):
    is_light_on = False
    is_light_off = True


class MicrowaveTime(object):
    def __init__(self):
        self.microwave_current_time = datetime.datetime.now().strftime('%H:%M')


class MicrowaveTimer(object):
    def __init__(self):
        pass


class Food(object):
    def __init__(self, cold):
        self.cold = FoodTemperature.is_cold


class Microwave(object):

    def __init__(self):
        self.is_on = False
        self.is_empty = True
        self.door = Door.is_closed
        self.light = Light.is_light_off
        self.m_time = MicrowaveTime().microwave_current_time

    def __str__(self):
        return "%s %s %s %s %s" % (self.is_on, self.is_empty, self.door, self.light, self.m_time)




