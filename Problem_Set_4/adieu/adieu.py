import inflect

def main():
    p = inflect.engine()

    names = get_names()

    farewell_message = format_farewell(names, p)

    print(farewell_message)

def get_names():
    names = []
    print("Enter names one per line (press Ctrl + D to finish): ")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass
    return names

def format_farewell(names, inflect_engine):
    if len(names) == 0:
        return "Adieu, adieu, to no one"
    elif len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    else:
        formatted_names = inflect_engine.join(names)
        return f"Adieu, adieu, to {formatted_names}"

if __name__ == '__main__':
    main()