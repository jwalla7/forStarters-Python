# Lists: ordered, mutable, allows duplicate elements
# List = myList[start: end: step]

burger_toppings = ["Cheese", "Lettuce", "Tomato", "Onion", "Pickles"]
burger_condiments = ["Ketchup", "Mustard", "Special Sauce"]
burger_sandwich = ["Beef Patty", "Sesame Seed Bun"]

# Order - Plain Cheese Burger
order_plain_burger = burger_sandwich

# Order - Cheese Burger
order_cheese_burger = burger_sandwich + burger_toppings + burger_condiments

# Order - Cheese Burger without Cheese
order_cheese_burger_without_cheese = []
if burger_toppings.__eq__("Cheese"):
    burger_toppings.remove("Cheese")
    order_cheese_burger_without_cheese = burger_sandwich + burger_toppings + burger_condiments

# Order - Cheese Burger without Cheese and Pickles
order_cheese_burger_without_cheese_pickles = burger_sandwich + burger_toppings[1:4] + burger_condiments

# Order Double Cheese Burger
order_double_cheese_burger = burger_sandwich + burger_toppings + burger_condiments
order_double_cheese_burger.append("Beef Patty (2)")
order_double_cheese_burger.append("Cheese (2)")
order_double_cheese_burger.sort()

# order_cheese_burger.clear()
# order_cheese_burger.sort()
# order_cheese_burger.reverse()


# Print To Console
print("Plain Burger: " + str(order_plain_burger))
print("Plain Burger Reversed: " + str(order_plain_burger[::-1]))


print("Cheese Burger: " + str(order_cheese_burger))
print("Cheese Burger without Cheese and Pickles: " + str(order_cheese_burger_without_cheese_pickles))
print("Cheese Burger without Cheese: " + str(order_cheese_burger_without_cheese))

print("Double Cheese Burger: " + str(order_double_cheese_burger))
