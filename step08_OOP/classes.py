#
# ? Create a simple class
# class Human:  # can also include round brackets # class Human():
#     name = "Saad"  # Class attribute


# human_1 = Human()  # Creating an instance of the class
# print(human_1.name)  # Outputs: Saad

# ? Create a Constructor Function
# The __init__ method, also known as the constructor, is called as soon as an instance of a class is created. It's used to initialize the object's attributes.


# class Human:
#     def __init__(self) -> None:
#         print("Hello I am a Human!")


# human_1 = Human()  # Outputs: Hello I am a Human!


# ? Pass an Argument to the Constructor Function
# You can pass arguments to the constructor to initialize the object's attributes with specific values.


# class Human:
#     def __init__(self, name: str) -> None:
#         print(f"Hello I am a Human and my name is {name}")


# human_1 = Human("Saad")  # Outputs: Hello I am a Human and my name is Saad


# ? What are Attributes

# Attributes are variables associated with a class or an instance of a class. They are accessed using the dot (.) notation.
# There are two main types of attributes in a class:

# ? Instance Attributes:

# Instance attributes are specific to an instance of a class. Each instance can have different values for these attributes.


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make  # Instance attribute
#         self.model = model  # Instance attribute
#         self.year = year  # Instance attribute


# my_car = Car("Toyota", "Corolla", 2022)
# print(my_car.make)  # Output: Toyota
# print(my_car.model)  # Output: Corolla

# ? Class Attributes:

# Class attributes are shared among all instances of a class. They are defined directly within the class and outside of any methods.

# class Car:
#     wheels = 4  # Class attribute

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year


# my_car = Car("Toyota", "Corolla", 2022)
# print(my_car.wheels)  # Output: 4

# another_car = Car("Honda", "Civic", 2021)
# print(another_car.wheels)  # Output: 4


# ? Define and Call a method of a class

# ? Note: Methods are functions defined inside a class. The first parameter of any method inside a class always refers to the instance of that class, usually named self.


# class Human:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         print(f"Hello my name is {name} and I am a Human.")

#     def greet(self):
#         print("Hi Mr.Human!")


# human_1 = Human("Saad")
# human_1.greet()  # Output: Hi Mr.Human!


# ? Access Constructor Parameters outside of the Constructor function

# You can access and use the constructor parameters by assigning them to instance attributes using self.


# class Human:
#     def __init__(self, name: str) -> None:
#         print(f"Hello my name is {name} and I am a Human.")
#         self.name = name

#     def greet(self):
#         print(f"Hi Mr.{self.name}")

#     def goodbye(self, local_name):
#         print(f"Good Bye Mr.{local_name}")


# human_1 = Human("Saad")
# human_1.greet()  # Output: Hi Mr.Saad
# human_1.goodbye("Adnan")  # Output: Good Bye Mr.Adnan


# ? Static Methods in a Python class

# "@staticmethod" is a method decorator that defines a method that does not operate on an instance or the class itself. It behaves like a regular function but resides within the class.


# class MathOperations:
#     @staticmethod
#     def add(a, b):
#         return a + b


# # Calling the static method without creating an instance of the class
# result = MathOperations.add(5, 3)
# print(result)  # Output: 8


# ? Class Methods in a Python class

# @staticmethod: It groups related functions within a class but does not interact with class or instance data.


# @classmethod: It operates at the class level, with access to class attributes, making it a true class-level method.


# class Example:
#     class_variable = 10

#     def __init__(self, value):
#         self.instance_variable = value

#     @staticmethod
#     def static_method(a, b):
#         # Does not access class or instance variables
#         return a + b

#     @classmethod
#     def class_method(cls, increment):
#         # Operates on class level, can access class_variable
#         cls.class_variable += increment
#         return cls.class_variable


# # Using @staticmethod
# print(Example.static_method(5, 3))  # Output: 8

# # Using @classmethod
# print(Example.class_method(5))  # Output: 15
