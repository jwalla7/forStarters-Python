temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <=30:
    print("The temperature is good today!")
    print(" go outside")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("stay inside")


if not(temp >= 0 and temp <=30):
    print("stay inside please")
elif not(temp < 0 or temp > 30):
    print(" go outside please")

