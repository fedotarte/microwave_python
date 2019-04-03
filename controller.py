import sys

from microwave import Microwave


class Controller:
    # TODO make this class as a singleton

    microwave = None

    def __init__(self):
        self.int_command_types = {
            0: self.init_the_microwave,
            1: self.switch_on_off,
            2: self.open_close_door,
            3: self.insert_food,
            # 4: self.set_timer,
            # 5: self.press_start,
            # 6: self.press_stop,
            # 7: self.check_time
        }

    # check the input is digit
    def get_choice_in_game(self, int_input):
        for key, value in self.int_command_types.items():
            if key == int_input:
                value()

    def check_correct_digit(self, inputed_text):
        try:
            int_input = int(inputed_text)
            self.get_choice_in_game(int_input)

        except Exception as e:
            print("you got an exception:" + str(e))
        finally:
            print("to quit press q, t orestart r")

    # running through the enum "int_command_types" to find the correct key and initialize the related method
    # in the main.py : get_choice_in_game(check_correct_digit(inputed_text))

    # initialize the microwave if it doesn't exist
    def init_the_microwave(self):
        if self.microwave is None:
            self.microwave = Microwave()
            print("Your microwave is here!: " + self.microwave.__str__())
        else:
            print("you already have the microwave: " + self.microwave.__str__())

    def switch_on_off(self):
        if not self.microwave.is_on:
            self.microwave.is_on = True
        else:
            self.microwave.is_on = False
        print("it's %s that microwave is on! " % self.microwave.is_on)

    def open_close_door(self):
        closed_door = self.microwave.door.is_closed.value
        if not closed_door:
            closed_door = True
            print("the door is closed!")
        else:
            closed_door = False  #door is opened
            print("the door is opened!")
        print("closed_door: " + id(closed_door), ", self.microwave.door.is_closed.value: " +  id(self.microwave.door.is_closed.value))

        return closed_door

    def insert_food(self, food):
        return True

    def microwave_exists(self, check_microwave):
        return self.microwave == check_microwave

    def quit(self, inputed_q):
        if inputed_q.to_upper_case == "q":
            exit()

