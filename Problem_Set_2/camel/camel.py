def main():

    camel_case = input("camelCase: ").strip()

    snake_case = convert(camel_case)
    print("snake_case: ", snake_case)

def convert(name):
    snake = ""
    for char in name:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake +=char
    return snake

if __name__ == "__main__":
    main()
