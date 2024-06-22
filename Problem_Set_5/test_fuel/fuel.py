def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            guage(percentage)
            break
        except(ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > y or y == 0:
            raise ValueError

        percentage = (x / y) * 100
        return round(percentage)
    except ValueError:
        raise ValueError("Invalid fraction")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

def guage(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == '__main__':
    main()
