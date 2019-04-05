from pyfiglet import Figlet


class SpecialArt:

    @staticmethod
    def print_text(text):
        custom_fig = Figlet(font='ucf_fan_')
        if type(text) == str and len(text) <= 20:
            print(custom_fig.renderText(text))
        else:
            print("too large text!")
