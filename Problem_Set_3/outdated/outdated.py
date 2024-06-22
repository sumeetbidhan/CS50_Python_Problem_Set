def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Enter a date MM/DD/YYYY or Month Day, Year: ").strip().lower()


        if '/' in date and date.count('/') == 2:
            divide = date.split('/')
            if len(divide) == 3:
                month, day, year = divide
                if month.isdigit() and day.isdigit() and year.isdigit():
                    month, day, year = int(month), int(day), int(year)x
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break


        elif ' ' in date and ',' in date:
            try:
                month_name, day_year = date.split(' ', 1)
                day_year = day_year.strip()
                if ',' in day_year:
                    day_str, year_str = day_year.split(', ')
                    if day_str.isdigit() and year_str.isdigit():
                        day, year = int(day_str), int(year_str)
                        if month_name.capitalize() in months:
                            month = months.index(month_name.capitalize()) + 1
                            if 1 <= day <= 31:
                                print(f"{year:04}-{month:02}-{day:02}")
                                break
            except ValueError:
                pass

        print("Invalid date format, please try again.")

if __name__ == '__main__':
    main()
