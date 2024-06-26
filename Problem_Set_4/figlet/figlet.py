import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]

        if font not in figlet.getFonts():
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)
    user_text = input("Enter the text to convert to ASCII art: ")

    ascii_art = figlet.renderText(user_text)

    print(ascii_art)

if __name__ == '__main__':
    main()
