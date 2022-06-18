# Named Tuples assign meaning to each position in a tuple,
#   can be used wherever regular tuples are used,
#     they add the ability to access fields by name,
#       they return a new tuple subclass used to create tuple-like objects that have fields

# https://docs.python.org/3/library/collections.html#collections.namedtuple

from collections import namedtuple

Point = namedtuple('Point', 'field_x, field_y')  # Creates subclass Point with field_names x,y

# field_names can be single string with each field_name separated by whitespace and/or commas,
#  for example: 'xy' or 'x, y'.
# field_names cannot start with underscore _ or be a keyword
#   such as class, for, return, global, pass or raise

point_0 = Point(1, field_y=-4)  # Creates instance of class Point with two field_names (positional or keyword arguments)
print(point_0)
print(point_0.field_x)  # Fields are accessible by name, (-1)
print(point_0.field_y)  # (-4)

field_x, field_y = point_0  # Can unpack like a regular Tuple
print(point_0)  # (1, -4)

add_point_0 = point_0[0] + point_0[1]  # Can access indices like plain Tuples (1, -4)
print(add_point_0)  # (-3)







