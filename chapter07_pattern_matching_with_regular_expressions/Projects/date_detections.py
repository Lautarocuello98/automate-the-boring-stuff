import re   

# Regular expression to validate basic date format: DD/MM/YYYY
date_regex = re.compile(r"""
^
(0?[1-9]|[12][0-9]|3[01])   # day: 1–31
/
(0?[1-9]|1[0-2])           # month: 1–12
/
([12][0-9]{3})             # year: 1000–2999
$
""", re.VERBOSE)


def validate_date(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)

    # Months with 30 days
    if month in (4, 6, 9, 11) and day > 30:
        return False
    
    # February handling (leap year vs non-leap year)
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return day <= 29
        else:
            return day <= 28
    return True


def main():
    date = input("give me a date (DD/MM/YYYY): ").strip()

    # First, validate format using regex
    match = date_regex.fullmatch(date)
    if not match:
        print("invalid format")
        return
    
    # Extract day, month, year from regex groups
    day, month, year = match.groups()

    # Perform logical validation (e.g., no 31st of February)
    if validate_date(day, month, year):
        print(f"is validated: {day}/{month}/{year}")
    else:
        print(f"invalid date: {day}/{month}/{year}")


if __name__ == "__main__":
    main()