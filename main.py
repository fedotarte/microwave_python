from controller import Controller
from microwave import Microwave
from textart import SpecialArt

spec_art = SpecialArt()

spec_art.print_text("microwave")

controller = Controller()


def play_game():
    input_command = ''
    while input_command.upper() != 'Q':
        input_command = input("input the required command: ")
        try:
            controller.check_correct_digit(input_command)
        except Exception as e:
            print("that;s too bad... we will try again!" + str(e))
            play_game()


play_game()

spec_art.print_text("bye!")
