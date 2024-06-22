def main():

    time_str = input("What time is it? ").strip()


    time = convert(time_str)


    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):

    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60.0



if __name__ == "__main__":
    main()
