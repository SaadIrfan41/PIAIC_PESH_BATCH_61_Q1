#
# ? Encapsulation restricts access to certain attributes or methods, providing control over the internal state of an object.


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Private attribute

#     # Method to access private attribute
#     def get_balance(self):
#         return self.__balance

#     # Setter method to modify private attribute
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited {amount}. New balance is {self.__balance}"
#         return "Invalid deposit amount"


# # Creating an object of BankAccount
# account = BankAccount("John", 1000)
# print(account.get_balance())  # Output: 1000
# print(account.deposit(500))  # Output: Deposited 500. New balance is 1500
# # print(account.__balance)    # This would raise an AttributeError


# ? Accessing Private Members of Parent Class


class Parent:
    def __init__(self):
        self.__private_attr = "I am private!"

    def get_private_attr(self):
        return self.__private_attr  # Correct way to access private attributes


class Child(Parent):
    def access_private(self):
        try:
            return self.__private_attr  # Attempt to access private attribute
        except AttributeError as e:
            return f"Cannot access private attribute: {e}"


parent = Parent()
child = Child()

# Accessing private attribute through the parent class
print(parent.get_private_attr())  # Works fine

# Trying to access private attribute directly in the child class
print(child.access_private())  # Fails
