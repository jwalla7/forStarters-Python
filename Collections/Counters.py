# class.collections.Counter([iterable-or-mapping])

from collections import Counter

# Counter is a Dictionary subclass for counting hashable objects.
# Counter objects inherit Dictionary Method functionality except two which work differently:
#   fromkeys, and update

#  https://docs.python.org/3/library/collections.html#counter-objects


a = "aaaaabbbbcccdde"
count_characters = Counter(a)
print("characters: " + str(count_characters))
print("characters_values: " + str(count_characters.values()))
print("characters_most_common: " + str(count_characters.most_common(1)))
print("characters_asList: " + str(list(count_characters.elements())))

count_colors = Counter()
for color in ['red', 'blue', 'red', 'green', 'green', 'green']:
    count_colors[color] += 1

print(count_colors)

