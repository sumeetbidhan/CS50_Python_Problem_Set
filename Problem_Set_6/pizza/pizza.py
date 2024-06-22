import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) !=2:
        print("Usage: python pizza.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("File does not exit")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)


            headers = data[0]
            rows = data[1:]


            table = tabulate(rows, headers, tablefmt='grid')
            print(table)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == '__main__':
    main()
