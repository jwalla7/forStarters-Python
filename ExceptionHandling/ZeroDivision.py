x = 42
y = 0

try:
    print(x / y)
except ZeroDivisionError as zE:
    print("Invalid divisor")
else:
    print("Invalid")
finally:
    print("This will always run at the end")