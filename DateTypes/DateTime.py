from datetime import datetime, timedelta

print("------ Example 0 ------")
current_date = datetime.now()
print("Today is", str(current_date))


print("------ Example 1 ------")
# timedelta is used to define a period of time. Also used for adding or removing microseconds, milliseconds, minutes, days or weeks of a date.
one_microsecond = timedelta(microseconds=1)
one_microsecond_ago = current_date - one_microsecond
print("One microsecond ago was", str(one_microsecond_ago))

one_millisecond = timedelta(milliseconds=1)
one_millisecond_ago = current_date - one_millisecond
print("One millisecond ago was", str(one_millisecond_ago))

one_minute = timedelta(minutes=1)
one_minute_ago = current_date - one_minute
print("A minute ago was", str(one_minute_ago))

one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday was", str(yesterday))

one_week = timedelta(weeks=1)
last_week = current_date - one_week
print("Last week was", str(last_week))

current_hour = current_date.hour  # Hour
current_day = current_date.day  # Day
current_month = current_date.month  # Month
current_year = current_date.year  # Year
print(f"Today is the day {current_day} of month {current_month} in {current_year} at hour {current_hour}")


print("------ Example 2 ------")
while True:
    birthday = input("When is your birthday (dd/mm/yyyy)?")
    try:
        birthday_date = datetime.strptime(birthday.lstrip(), '%d/%m/%Y')
        if birthday.format('%d/%m/%Y'):
            print("Birthday:", str(birthday_date))

            break
    except ValueError:
        print("Invalid, please enter integers in format: dd/mm/yyyy")

        continue
    finally:
        pass


