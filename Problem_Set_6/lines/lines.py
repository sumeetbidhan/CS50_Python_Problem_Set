import sys
import os

def main():
    if len(sys.argv) !=2:
        print("Usage: python lines.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]


    if not filename.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("File does not exist")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


    count = 0

    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            count += 1

    print(count)

if __name__ == '__main__':
    main()
