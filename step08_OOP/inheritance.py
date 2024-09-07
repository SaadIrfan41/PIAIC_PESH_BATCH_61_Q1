#
# ? Inheritance in Python.

# Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse and creating a hierarchical relationship between classes.

#  There are 3 types of Inheritance:

# ? Single Inheritance

# Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic sound"


# # Child class inheriting from Animal
# class Dog(Animal):
#     def dog_name(self):
#         return f"{self.name} says Hi!"


# # Creating an object of the Dog class
# dog = Dog("Buddy")
# print(dog.dog_name())  # Output: "Buddy says Hi! "
# print(dog.speak())  # Output: "Some generic sound"

# ? Multilevel Inheritance

# Multilevel inheritance is when a class inherits from a parent class, and then another class inherits from that child class, creating a chain of inheritance.

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic sound"


# # Derived class inheriting from Animal
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"


# # Another derived class inheriting from Dog
# class Puppy(Dog):
#     def play(self):
#         return f"{self.name} is playing!"


# # Creating an object of the Puppy class
# puppy = Puppy("Buddy Jr.")
# print(puppy.speak())  # Output: Buddy Jr. says Woof!
# print(puppy.play())  # Output: Buddy Jr. is playing!


# ? Multiple Inheritance

# Multiple inheritance is when a class inherits from more than one parent class. It allows the child class to inherit attributes and methods from multiple classes.

# # Parent class 1
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic sound"


# # Parent class 2
# class Walker:
#     def walk(self):
#         return "I can walk"


# # Child class inheriting from both Animal and Walker
# class Dog(Animal, Walker):
#     def speak(self):
#         return f"{self.name} says Woof!"


# # Creating an object of the Dog class
# dog = Dog("Buddy")
# print(dog.speak())  # Output: Buddy says Woof!
# print(dog.walk())  # Output: I can walk


# ? Method Overriding

# Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class

# # Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic sound"


# # Child class inheriting from Animal
# class Dog(Animal):
#     # Overriding the speak method of the parent class
#     def speak(self):
#         return f"{self.name} says Woof!"


# # Creating an object of the Dog class
# dog = Dog("Buddy")
# print(dog.speak())  # Output: Buddy says Woof!


# ? Accessing Parent Class Attributes in Python

# In Python, super() is a built-in function used in classes to call methods from a parent class, allowing you to access and extend the functionality of inherited methods. It is particularly useful in inheritance scenarios, especially when dealing with method overriding and multiple inheritance.

# ? Example of super() in Single Inheritance
# # Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic sound"


# # Child class inheriting from Animal
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Calling the parent class's __init__ method
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         # Extending the functionality of the parent's speak method
#         return super().speak() + " But I prefer barking!"


# # Creating an object of the Dog class
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.speak())  # Output: Some generic sound But I prefer barking!


# ? Example of super() in Multiple Inheritance

# # Base class 1
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic sound"


# # Base class 2
# class Walker:
#     def __init__(self):
#         self.walk_style = "Walking on four legs"


# # Child class inheriting from both Animal and Walker
# class Dog(Animal, Walker):
#     def __init__(self, name, breed):
#         # Calling the __init__ methods of both parent classes
#         super().__init__(name)  # This will follow MRO (Method Resolution Order)
#         Walker.__init__(self)  # Direct call to the Walker class init
#         self.breed = breed

#     def speak(self):
#         return super().speak() + " Woof!"


# # Creating an object of the Dog class
# dog = Dog("Buddy", "Labrador")
# print(dog.speak())  # Output: Some generic sound Woof!
# print(dog.walk_style)  # Output: Walking on four legs
