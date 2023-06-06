from datetime import datetime, timedelta


def current_date(present_date):
    if present_date.year != datetime.now().year:
        print("Please select the current date")
    return present_date


def remaining_months_in_current_year(current_date):
    print("--- Remaining months of this year ---")
    if current_date.year == datetime.now().year:
        while current_date.year == datetime.now().year:
            print(str(current_date))

            current_date += timedelta(weeks=4, days=2)
        return "Complete"


print(remaining_months_in_current_year(current_date(datetime.now())))


def remaining_months_in_any_year():
    print("--- Remaining months in any year ---")
    while True:
        user_input_date = input("Enter a date dd/mm/yyyy \n")
        try:
            user_date = datetime.strptime(user_input_date.lstrip(), '%d/%m/%Y')
            if user_input_date.format('%d/%m/%Y'):
                next_year = user_date.year + 1
                while user_date.year < next_year:
                    print(str(user_date))

                    user_date += timedelta(weeks=4, days=3)
            break
        except ValueError:
            print("Invalid, please enter a valid date in format: dd/mm/yyyy")

            continue
        finally:
            pass # checks nothing
    return "Complete"


print(remaining_months_in_any_year())