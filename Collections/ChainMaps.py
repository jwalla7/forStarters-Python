#  class.collections.ChainMap(*maps)

from collections import ChainMap, Counter

#  ChainMaps group multiple Dictionaries or other mappings together to create a single
#    mutable view. If no maps are specified, a single empty Dictionary is provided
#      so that the new chain has at least one mapping.

#  ChainMap is often faster than creating new Dictionaries and running multiple dict.update() calls
#  ChainMap creates a view over multiple mappings.

#  ChainMap underlying mappings are stored in a List which is public and can be accessed,
#    or updated using the maps attribute. There is no other state.

from timeit import default_timer as runtime_timer

dictionary_0 = dict(a=1, b=2, c=3)
dictionary_1 = dict(d=3, e=4)
dictionary_2 = dict(f=5, g=6, h=7)
dictionary_4 = Counter(['i', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
                        'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j'])

# Usually Slower Practice: Create a new Dictionary containing combines dictionaries

start = runtime_timer()
outer_dictionary = {**dictionary_0, **dictionary_1, **dictionary_2, **dictionary_4}  # Combines Dictionaries
print(outer_dictionary)
stop = runtime_timer()
print('   runtime: ' + str(stop - start))

# Usually Faster Practice: ChainMap
start = runtime_timer()
chain = ChainMap(dictionary_0, dictionary_1, dictionary_2, dictionary_4)  # Chains each Dictionary
print(chain)
stop = runtime_timer()
print('   runtime: ' + str(stop - start))

for key, value in chain.items():
    print(f"{key}: {value}")

print("ChainMap Maps: " + str(chain.maps))
print("ChainMap Parents: " + str(chain.parents))


