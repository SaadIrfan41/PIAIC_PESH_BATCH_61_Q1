#
# ? List in python
shopping_list = ["milk", "bread", "eggs", "bananas"]

# ? Accessing items in a list
print(shopping_list[0])  # Output: milk

# ? Modifying items in a list
shopping_list[0] = "apple"
print(shopping_list)  # Output: ['apple', 'bread', 'eggs', 'bananas']

# ? Adding items to a list
shopping_list.append("oranges")
print(shopping_list)

# ? Removing items from a list
shopping_list.remove("bread")
print(shopping_list)

# ? Total items in the list
print("Total Items: ", len(shopping_list))
