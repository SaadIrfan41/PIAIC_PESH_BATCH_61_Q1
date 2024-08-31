#
# ? A set is an unordered collection of unique elements.
my_set = {1, 2, 3, "apple", "banana"}

# ? Characteristics:

# ? Mutable: You can add or remove elements from a set.

my_set = {1, 2, 3}
# Adding an element to the set
my_set.add(4)  # my_set becomes {1, 2, 3, 4}

# Removing an element from the set
my_set.remove(2)  # my_set becomes {1, 3, 4}

# ? No Duplicates: A set cannot contain duplicate values.

# Attempting to add duplicate values does not change the set
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # Output: {1, 2, 3}

# ? Unordered: Sets do not maintain the order of elements.

my_set = {"red", "green", "blue"}
# Order of elements is not guaranteed
print(my_set)  # Output could be {'green', 'blue', 'red'} or any other order

# ? Membership Test: You can check if an element exists in a set.

my_set = {1, 2, 3, 4, 5}

# Checking if a value exists in the set
is_three_in_set = 3 in my_set  # True
is_six_in_set = 6 in my_set  # False

# ? The len() function can be used to find the number of elements in a set.

my_set = {1, 2, 3, 4, 5}

# Finding the number of elements in the set
set_length = len(my_set)
print(set_length)  # Output: 5

# ? You can use set operations like union, intersection, and difference.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union of sets
print(set_a.union(set_b))
union_set = set_a | set_b  # {1, 2, 3, 4, 5}

# Intersection of sets
print(set_a.intersection(set_b))
intersection_set = set_a & set_b  # {3}

# Difference of sets
print(set_a.difference(set_b))
difference_set = set_a - set_b  # {1, 2}
