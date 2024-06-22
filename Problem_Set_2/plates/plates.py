def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    found_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            found_number = True
            if s[i] == '0':
                return False
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            break

    return True

if __name__ == '__main__':
    main()
