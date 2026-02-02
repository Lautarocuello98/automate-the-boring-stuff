import re   

# regex con anclajes
date_regex = re.compile(r"""
^
(0?[1-9]|[12][0-9]|3[01])   # día: 1–31
/
(0?[1-9]|1[0-2])           # mes: 1–12
/
([12][0-9]{3})             # año: 1000–2999
$
""", re.VERBOSE)


def validate_date(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)

    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return day <= 29
        else:
            return day <= 28
    return True


def main():
    date = input("give me a date (DD/MM/YYYY): ").strip()

    match = date_regex.fullmatch(date)
    if not match:
        print("invalid format")
        return

    day, month, year = match.groups()

    if validate_date(day, month, year):
        print(f"is validated: {day}/{month}/{year}")
    else:
        print(f"invalid date: {day}/{month}/{year}")


if __name__ == "__main__":
    main()