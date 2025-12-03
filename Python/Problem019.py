"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

MONTHS = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}

MONTHS_LY = {
    "Jan": 31,
    "Feb": 29,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def iterate_days(first_day: int, days: int, sunday_count: int):
    for day in range(days):
        if first_day == 1:
            # print(f"Monday, day {day}")
            first_day += 1
        elif first_day == 2:
            # print(f"Tuesday, day {day}")
            first_day += 1
        elif first_day == 3:
            # print(f"Wednesday, day {day}")
            first_day += 1
        elif first_day == 4:
            # print(f"Thursday, day {day}")
            first_day += 1
        elif first_day == 5:
            # print(f"Friday, day {day}")
            first_day += 1
        elif first_day == 6:
            # print(f"Saturday, day {day}")
            first_day += 1
        elif first_day == 7:
            print(f"Sunday, day {day}")
            if day == 0:
                sunday_count += 1
                print("Counting this Sunday!!")
            first_day = 1
    return first_day, sunday_count

def main():
    sunday_count = 0
    first_day = 1
    for year in range(1900, 2001):
        if year == 1901:
            sunday_count = 0
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            for month, days in MONTHS_LY.items():
                print(f"Leap year {year}. Month {month} has {days}.")
                first_day, sunday_count = iterate_days(first_day=first_day,
                                                       days=days,
                                                       sunday_count=sunday_count)
        else:
            for month, days in MONTHS.items():
                print(f"Year {year}. Month {month} has {days}.")
                first_day, sunday_count = iterate_days(first_day=first_day,
                                                       days=days,
                                                       sunday_count=sunday_count)
    print(f"Number of sundays is {sunday_count}")


if __name__ == '__main__':
    main()
