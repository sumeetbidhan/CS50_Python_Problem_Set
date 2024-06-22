def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check the length of the plate
    if not (2 <= len(s) <= 6):
        return False

    # Check the first two characters are alphabetic
    if not s[:2].isalpha():
        return False

    # Check the entire plate is alphanumeric
    if not s.isalnum():
        return False

    # Initialize found_number flag
    found_number = False

    # Check for number placement and leading zero in numbers
    for i in range(len(s)):
        if s[i].isdigit():
            found_number = True
            if s[i] == '0' and not any(char.isdigit() for char in s[:i]):
                return False
            # All following characters must be digits
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            break

    return True

if __name__ == '__main__':
    main()
