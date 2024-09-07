    #
# ? A dictionary is an ordered, mutable collection of key-value pairs.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# ? You can access the value associated with a specific key using square brackets [].
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])  # Output: 30

# ? You can add a new key-value pair or update the value of an existing key.
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating the value of an existing key

print(my_dict)
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# ? You can remove a key-value pair using the del keyword or the pop() method.
del my_dict["city"]  # Remove the 'city' key-value pair
print(my_dict)
# Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

email = my_dict.pop("email")  # Remove and return the 'email' value
print(email)  # Output: alice@example.com
print(my_dict)
# Output: {'name': 'Alice', 'age': 31}

# ? You can check if a key exists in a dictionary using the in keyword.

if "name" in my_dict:
    print("Name is present")  # Output: Name is present

if "city" not in my_dict:
    print("City is not present")  # Output: City is not present

# ? You can iterate over the keys, values, or key-value pairs in a dictionary.

# ? Iterate over keys:
for key in my_dict:
    print(key)
# Output:
# name
# age

# ? Iterate over values:
for value in my_dict.values():
    print(value)
# Output:
# Alice
# 31

# ? Iterate over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 31


# ? Characteristics:

# ? Mutable: You can change, add, or remove key-value pairs.

my_dict = {"name": "Alice", "age": 30}

# Adding a new key-value pair
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Changing the value of an existing key
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

# ? No Duplicate Keys: Keys must be unique.

my_dict = {"name": "Alice", "age": 30, "name": "Bob"}

# The second "name" key overwrites the first one
print(my_dict)  # Output: {'name': 'Bob', 'age': 30}


# ? Key-Value Pair: Each element consists of a key and a value.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# 'name' is a key with the value 'Alice'
# 'age' is a key with the value 30
# 'city' is a key with the value 'New York'

# ? The items() method in a Python dictionary returns a view object that displays a list of a dictionary's key-value tuple pairs.

# ? What my_dict.items() Does:

# ? Returns Key-Value Pairs: It provides a view of the dictionary’s items as tuples, where each tuple consists of a key and its corresponding value.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

items_view = my_dict.items()

# Print the view object
print(items_view)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Iterate over the key-value pairs
for key, value in items_view:
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: name, Value: Alice
# Key: age, Value: 30
# Key: city, Value: New York

# ? View Object: This view object reflects the dictionary’s current state. If the dictionary changes, the view object reflects those changes.

# Create an initial dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Get the view object of key-value pairs
items_view = my_dict.items()

# Print the initial view object
print("Initial view object:", items_view)
# Output: Initial view object: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Modify the dictionary
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating an existing key-value pair
del my_dict["city"]  # Removing a key-value pair

# Print the updated view object
print("Updated view object:", items_view)
# Output: Updated view object: dict_items([('name', 'Alice'), ('age', 31), ('email', 'alice@example.com')])

# Iterate over the updated view object
for key, value in items_view:
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: name, Value: Alice
# Key: age, Value: 31
# Key: email, Value: alice@example.com

# Using Dictionary Methods

# ? Dictionaries come with several useful methods, such as get(), keys(), values(), items(), and clear().

# ? get(): Returns the value for a key, or None (or a specified default value) if the key is not found.
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("city", "Not Found"))  # Output: Not Found

# ? keys(): Returns a view object containing the dictionary's keys.
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
# ? values(): Returns a view object containing the dictionary's values.
print(my_dict.values())  # Output: dict_values(['Alice', 31])
# ? items(): Returns a view object containing the dictionary's key-value pairs.
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31)])
# ? clear(): Removes all key-value pairs from the dictionary.
my_dict.clear()
print(my_dict)  # Output: {}
