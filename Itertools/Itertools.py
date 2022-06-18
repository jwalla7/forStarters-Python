# Itertools contains iterator Methods for efficient looping

from itertools import count, cycle, repeat, accumulate, chain, compress, dropwhile, filterfalse, groupby, islice, starmap, takewhile, tee, zip_longest, product, permutations, combinations, combinations_with_replacement

# https://docs.python.org/3/library/itertools.html#module-Itertools

# Product: equivalent to nested for loop,
#   itertools.product(*iterables, repeat=1)
a = [1, 2]
b = [3, 4]
product_sequence_0 = product(a, b)
print(list(product_sequence_0))

c = [5, 6]
d = [7]
product_sequence_1 = product(c, d, repeat=3)
print(list(product_sequence_1))



