from controller import Controller
from textart import SpecialArt

SpecialArt.print_text("microwave")

controller = Controller()


def play_game():
    print("to quit press q, to restart press r ")
    input_command = ''
    while input_command.upper() != 'Q':
        input_command = input("input the required command: ")
        try:
            controller.check_correct_digit(input_command)
        except Exception as e:
            print("main error... we will try again!" + str(e))
            # рекурсия типа)
            play_game()


play_game()
