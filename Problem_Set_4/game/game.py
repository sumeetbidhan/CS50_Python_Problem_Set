import random

def main():
    level = get_level()
    number_to_guess = random.randint(1,level)
    guess_number(number_to_guess)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass
def guess_number(number_to_guess):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < number_to_guess:
                    print("Too small!")
                elif guess > number_to_guess:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass

if __name__ == '__main__':
    main()