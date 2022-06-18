# class.collections.defaultdict(default_factory=None,/[,...])

from collections import defaultdict

#  Generates a default key when missing, using the __missing__(key) Method.
#    The __missing__ method initalizes the default_factory attribute to the constructor
#      if present, or to None, if absent.

#   https://docs.python.org/3/library/collections.html#defaultdict-objects

default_key = defaultdict(float)
default_key['a'] = 1
default_key['b'] = 2
generate_default_key = default_key['c']
print(default_key)
print(generate_default_key)


