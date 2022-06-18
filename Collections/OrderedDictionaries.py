#  class.collections.OrderedDict([items])

#    Returns an instance of a Dictionary subclass that has methods specialized from
#      rearranging dictionary order.
#  They have become less important since the built-in Dictionary now can remember insertion order (Python 3.7)

#  https://docs.python.org/3/library/collections.html#ordereddict-objects


from collections import OrderedDict
ordered_dictionary_0 = OrderedDict()

ordered_dictionary_0['item_1'] = 'A'
ordered_dictionary_0['item_2'] = 'b'
ordered_dictionary_0['item_3'] = "3"
ordered_dictionary_0['item_4'] = 4
ordered_dictionary_0['item_5'] = 5
ordered_dictionary_0['item_6'] = 6
ordered_dictionary_0['item_7'] = 7

print(ordered_dictionary_0)

