x = "hello"[0]
print(x)

class Person:
    def __init__(self):
        pass


class Employment(Person):
    def __init__(self, value, profession):
        self.profession = profession
        # Person.__init__(self)
        super().__init__(value)


class Identity(Person, Employment):
    def __init__(self, value, social_security_number):
        self.social_security_number = social_security_number
        super().__init__(value)


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
