def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()

            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            print()
            break

    sorted_items = sorted(grocery_list.keys())

    for item in sorted_items:
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == '__main__':
    main()
