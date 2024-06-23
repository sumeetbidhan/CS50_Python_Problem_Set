from datetime import date
import sys
import inflect

def main():
    birthdate = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birthdate = validate(birthdate)
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birthdate)
    minutes_word = convert_minutes(minutes)

    print(minutes_word)

def validate(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        return date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date format")

def calculate_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    return delta.days * 24 * 60

def convert_minutes(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").replace(",", "")
    return words

if __name__ == "__main__":
    main()
