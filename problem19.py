def days_in_month(month, year):
    if month == 1 and year % 4 == 0:
        return 29
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 6
month = 0
year = 1901
count = 0
while year < 2001:
    while month < 12:
        while day <= days_in_month(month, year):
            if day == 1:
                count += 1
            day += 7
        day = day - days_in_month(month, year)
        month += 1
    month = 0
    year += 1
print count


