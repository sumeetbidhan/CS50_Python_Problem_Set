import sys
import csv
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input_csv> <output_csv>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.isfile(input_filename):
        print(f"Could not read {input_filename}")
        sys.exit(1)

    students = []
    try:
        with open(input_filename, 'r') as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last, first = row['name'].rstrip().split(", ")
                house = row['house']
                students.append({"first": first, "last": last, "house": house})
    except Exception as e:
        print(f"Could not read {input_filename}")
        sys.exit(1)

    try:
        with open(output_filename, 'w', newline='') as output_file:  # Fixed variable name
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            writer.writeheader()
            for student in students:
                writer.writerow(student)
    except Exception as e:
        print(f"Could not write to {output_filename}")
        sys.exit(1)

if __name__ == '__main__':
    main()

