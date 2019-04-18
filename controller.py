import os
import sys

import psutil
import logging

from microwave import Microwave
from textart import SpecialArt


class Controller:
    # TODO make this class as a singleton

    microwave = None

    def __init__(self):

        self.string_command_types = {
            'q': self.quit_microwave,
            'r': self.restart_microwave
        }

        self.int_command_types = {
            0: self.init_the_microwave,
            1: self.switch_on_off,
            2: self.open_close_door,
            3: self.insert_food,
            4: self.set_timer
            # 5: self.press_start,
            # 6: self.press_stop,
            # 7: self.check_time
        }

    # check the input is digit
    def get_str_commands(self, str_input):
        for key, value in self.string_command_types.items():
            is_ok = False
            if key == str_input:
                is_ok = True
                value()
        return is_ok

    def get_choice_in_game(self, int_input):
        is_ok = False
        for key, value in self.int_command_types.items():
            if key == int_input:
                is_ok = True
                value()
        return is_ok
    #TODO refactor: 1) check_correct_digit(...) should return bool, check it out from the main.py
    def check_correct_digit(self, inputed_text):
        try:
            int_input = int(inputed_text)
            if not self.get_choice_in_game(int_input):
                max_key = max(map(int, self.int_command_types))
                print("print from 0 to", str(max_key))

        except ValueError as e:
            print("it's not an Integer.. we will try to check it out...")
            try:
                if not self.get_str_commands(inputed_text):
                    print("type q or r!")
            except Exception as ex:
                print("the command is not correct! " + str(ex))

    # running through the enum "int_command_types" to find the correct key and initialize the related method
    # in the main.py : get_choice_in_game(check_correct_digit(inputed_text))

    # initialize the microwave if it doesn't exist
    def init_the_microwave(self):
        if self.microwave is None:
            self.microwave = Microwave()
            print("Your microwave is here!: " + self.microwave.__str__())
        else:
            print("you already have the microwave: " + self.microwave.__str__())

    def switch_on_off(self): #а при выключении микроволновки никакого сообщения не выдается?

        if not self.microwave.is_on:
            self.microwave.is_on = True
            print("it's %s that microwave is on! " % self.microwave.is_on)

        else:
            self.microwave.is_on = False
            print("it's %s that microwave is off! " % self.microwave.is_off)

    def open_close_door(self):
        if not self.microwave.door.is_closed:
            self.microwave.door.is_closed = True
            print("the door is closed!")
        else:
            # self.microwave.door.is_closed.value = False  # door is opened
            self.microwave.door.is_closed= False
            print("the door is opened!")

    def insert_food(self):
        if not self.microwave.is_empty and self.microwave.door.is_closed:
            self.microwave.is_empty = False
            print("the food inside!")
        else:
            #TODO ЛИЗЕ поставь проверку на дверь, когда забираем еду
            #так уже же есть проверка выше или че
            self.microwave.is_empty = True
            print("you've got the food!")

    def microwave_exists(self, check_microwave):
        return self.microwave == check_microwave

    #TODO ЛИЗЕ поставить обработку параметра с клавиатуры, чтобы устанавливать время таймера
    def set_timer(self):
        data = input("Enter a number: ")
        self.microwave.m_timer.start(int(data))

    # def set_timer(self):
    #     import time
    #     print('Hello')
    #     time.sleep(5)  # number of seconds
    #     print('Bye')
    #
    # def set_timer(self, seconds):
    #     import time
    #     if seconds>0:
    #         print('Hello')
    #         time.sleep(seconds)  # number of seconds
    #         print('Bye')

    def restart_microwave(self):
        print()
        SpecialArt.print_text("restart!")
        try:
            p = psutil.Process(os.getpid())
            for handler in p.open_files() + p.connections():
                os.close(handler.fd)
        except Exception as e:
            logging.error(e)

        python = sys.executable
        os.execl(python, python, *sys.argv)

    def quit_microwave(self):
        SpecialArt.print_text("bye!")
        exit()
