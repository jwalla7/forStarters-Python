class Person:
    def __init__(self):
        pass


class Employment(Person):
    def __init__(self):
        Person.__init__(self)


class Identity(Person):
    def __init__(self):
        Person.__init(self)


class AccountType:
    # Checking
    # Savings
    # Preferred
    def __init__(self):
        pass


class AccountUsers(Person):
    def __init__(self):
        pass


class OwnershipType:
    # Individual
    # Joint
    def __init__(self):
        pass


class AccountOwner(Person):
    # Authorization
    # Number of Owners
    def __init__(self):
        pass
