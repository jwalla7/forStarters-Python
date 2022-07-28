#  An anonymous inline function consisting of a single expression which is evaluated when the function is called.
#    lambda [parameters]: expression

multiply_two_numbers = lambda x, y: x * y
print(multiply_two_numbers(2, 3))

power = lambda x, y: x ** y
print(power(2, 2))

print("------ Example ------")
operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "highest": lambda seq: max(seq),
    "lowest": lambda seq: min(seq)
}

students = [
    {"name": "Robert", "grades": (67, 78, 90, 100)},
    {"name": "Jennifer", "grades": (45, 78, 84, 99)},
    {"name": "Greg", "grades": (98, 78, 95, 87)},
    {"name": "Mariah", "grades": (89, 100, 57, 67)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', 'highest', or 'lowest': ")

    result = operations[operation](grades)
    print(result)