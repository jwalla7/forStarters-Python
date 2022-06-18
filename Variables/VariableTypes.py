name = "Jamal"
lastName: str = "Wallace"


def myName(fName, lName) -> str:
    return fName + " " + lName


print(myName(name, lastName))