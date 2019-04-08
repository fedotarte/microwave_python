import datetime
import time
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
    microwave_last_time = datetime.datetime.now().time()

    def __init__(self):
        self.microwave_current_time = datetime.datetime.now().time()
    #.strftime('%H:%M') add to to print time
    def check_time(self):
        if self.microwave_last_time < self.microwave_current_time:
            self.microwave_last_time = datetime.datetime.now().time()
            return self.microwave_last_time


class MicrowaveTimer(object):
    def __init__(self):

        self.timer_inc = 0

    def start(self, seconds):
        if self.timer_inc != 0:
            self.timer_inc = 0
        while seconds > 0:
            print("1 second passed")
            time.sleep(1)
            self.timer_inc += 1
            seconds -= self.timer_inc
            print("seconds remaining: " + seconds)


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
        self.m_timer = MicrowaveTimer()

    def __str__(self):
        return "%s %s %s %s %s" % (self.is_on, self.is_empty, self.door, self.light, self.m_time)


class Food(object):
    pass
