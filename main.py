from controller import Controller
from microwave import Microwave
from textart import SpecialArt

spec_art = SpecialArt()

spec_art.print_text("microwave")

controller = Controller()

input_command = ''
while input_command.upper() != 'Q':
    input_command = input("input the required command: ")
    controller.check_correct_digit(input_command)
