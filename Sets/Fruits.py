"""
Set Types: set, frozenset
set: unordered, immutable, no duplicates
frozenset: unordered, immutable, no duplicates, and can be used as a dictionary key or as an element of another set
"""


unique_characters_in_hello = set("hello")
print("Unique characters in Hello: " + str(unique_characters_in_hello))
print("------ ------")

fruits = {"Avocado", "Pineapple", "Apple", "Lime", "Grapes", "Peach", "Plum", "Banana", "Kiwi"}
more_fruits = set((["Avocado", "Cantaloupe"]))
junk_foods = {"Potato Chips", "Glazed Donut", "Oreo", "Twinkies", "M&Ms", "Pop Tarts", "Snickers Bar"}

junk_foods.clear()

more_fruits.add("Mango")
more_fruits.add("Orange")
more_fruits.add("Lemon")
more_fruits.add("Grapefruit")
more_fruits.add("Pear")
more_fruits.add("Melon")
more_fruits.add("Watermelon")

# Remove "Melon" value
more_fruits.discard("Melon")

# Union combines two sets and excludes values that have duplicates
fruit_platter = fruits.union(more_fruits)

print("fruits: " + str(fruits))
print("more_fruits: " + str(more_fruits))
print()

# Print values of fruit_platterr
for f in fruit_platter:
    print("fruit_platter: " + str(f))
print()

# Find Duplicates - Intersection combines and outputs duplicate values between two sets
print("------ Duplicate value in fruits and more_fruits ------")
print(fruits.intersection(more_fruits))

# Print what fruits have that more_fruits don't have
print("------ Values fruits have that more_fruits do not have ------")
print(fruits.difference(more_fruits))







