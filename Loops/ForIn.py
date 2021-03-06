import time

# Combine Lists
fruits = ["Apple", "Cantaloupe", "Banana"]
fruits_colors = ["Red", "Orange", "Yellow"]
fruits_minerals = ["Fiber", "Folate", "Potassium"]

i = 0
fruits_info = []
for fruit in fruits:
    colors = fruits_colors[i]
    minerals = fruits_minerals[i]
    fruits_info.append((fruit, colors, minerals))
    i += 1

zip_fruits_info = (list(zip(fruits,fruits_colors, fruits_minerals )))

print(fruits_info)
print("for-in: " + str(list(fruits_info)))
print("zip: " + str(zip_fruits_info))


# Increment from 0 to 9, print two parallel columns
for i in range(10):
    print(i, i)

increment_by_two_to_ten_string = ", ".join(format(i) for i in range(10))
print(increment_by_two_to_ten_string)

# Decrement by 1 starting from 10, print Go at 0, wait .25 sec after each print
for i in range(10, 0, -1):
    print(i, end=" ")
    time.sleep(0.25)
print("Go!")

# Don't print even numbers
skipEven = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in skipEven:
    if i % 2 == 0:
        pass
    else:
        print(i, end=" ")
        time.sleep(0.25)
print()

# Print str without -
phone_number = "803-742-7777"

for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ")
    time.sleep(0.25)
print()


rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
character = input("Enter a character to use: ")

for i in range(rows):
    for j in range(columns):
        print(character, end="")
    print()
