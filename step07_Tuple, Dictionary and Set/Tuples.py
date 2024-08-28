#
# ? A tuple is an immutable, ordered collection of elements.
my_tuple = (1, 2, 3, "apple", "banana")

# ? Characteristics:

# ? Immutable: Once created, the elements cannot be modified.

# my_tuple = (1, 2, 3)
# # Attempting to change an element will raise an error
# my_tuple[0] = 10  # This will raise a TypeError

# ? Allows Duplicates: Can contain duplicate values.

# This tuple contains duplicate values (2, 2) and (3, 3, 3)
my_tuple = (1, 2, 2, 3, 3, 3)

# ? Indexed: You can access elements by their index.

my_tuple = ("red", "green", "blue")
# Accessing elements by their index
first_color = my_tuple[0]  # 'red'
second_color = my_tuple[1]  # 'green'
third_color = my_tuple[2]  # 'blue'

# ? The count() method in a tuple is used to count the number of times a specified element appears in the tuple.

my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)

# Count how many times the number 2 appears in the tuple
count_of_twos = my_tuple.count(2)
print(count_of_twos)  # Output: 2

# Count how many times the number 4 appears in the tuple
count_of_fours = my_tuple.count(4)
print(count_of_fours)  # Output: 3

# Count how many times the number 6 appears in the tuple (which is not in the tuple)
count_of_sixes = my_tuple.count(6)
print(count_of_sixes)  # Output: 0
