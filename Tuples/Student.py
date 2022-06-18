student = ("James", 23, "Male", True)

print(student.count("James"))
print(student.index("Male"))

for s in student:
    print(s)

if "James" in student:
    print("James is here")

