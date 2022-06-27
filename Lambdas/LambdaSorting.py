#  Lists have a built-in list.sort() method that modifies the list in-place.
#    There is also a sorted() a built-in function which creates a new sorted list from an iterable.
#      sorted(iterable, /, key=None, reverse=False)


#  https://docs.python.org/3/library/functions.html#sorted
#  https://docs.python.org/3/howto/sorting.html


daily_event_attendance = [349, 935, 735, 539, 397]
print(sorted(daily_event_attendance))

daily_event_attendance.sort(key=lambda attendees: attendees * 2)  # sorts unchanged data by the results of an applied function


monthly_event_attendance = [('Jan', 349), ('Feb', 935), ('Mar', 735), ('Apr', 539), ('May', 397)]

print(monthly_event_attendance)
print(sorted(monthly_event_attendance, key=lambda x: x[1]))  # sorts by the index[1] of each key value pair
print(sorted(monthly_event_attendance, key=lambda k: k[0]))  # sorts by the index[0] of each key value pair
