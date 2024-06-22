import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"

    match = re.fullmatch(pattern, s, re.IGNORECASE)
    if not match:
        raise ValueError("Invalid format")

    start_hr, start_min, start_period, end_hr, end_min, end_period = match.groups()

    start_hr = int(start_hr)
    end_hr = int(end_hr)
    start_min = int(start_min)
    end_min = int(end_min)

    if not (1 <= start_hr <= 12 and 0 <= start_min < 60 and 1 <= end_hr <= 12 and 0 <= end_min < 60):
        raise ValueError("Invalid time value")

    start_hr_24 = convert_24(start_hr, start_period)
    end_hr_24 = convert_24(end_hr, end_period)

    start_time = f"{start_hr_24:02}:{start_min:02}"
    end_time = f"{end_hr_24:02}:{end_min:02}"

    return  f"{start_time} to {end_time}"

def convert_24(hour, period):
    if period == "AM":
        if hour == 12:
            return 0
        else:
            return hour
    else:
        if hour == 12:
            return 12
        else:
            return hour + 12

if __name__ == '__main__':
    main()






