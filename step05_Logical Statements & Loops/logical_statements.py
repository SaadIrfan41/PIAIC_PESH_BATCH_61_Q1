#
# ? Note that an any input entered by the user is a string unless set to a different DataType explicitly.
name: str = input("What is your name?")
# age: int = int(input("How old are you?"))
age = input("How old are you?")

# ? Check if name is string of alphabets name.isalpha()
# ? Check if age is number age.isdigit()

# # ? Simple if-else statement
if int(age) >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# # ? Simple if-else statement
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are not an adult.")

# # ? Nested if-else statement
# if age >= 18:
#     if age > 60:
#         print("You are a senior citizen.")
#     else:
#         print("You are an adult.")

# ? elif statement:
# if age < 60:
#     print("You are a senior citizen.")
# elif age >= 18:
#     print("You are an adult.")

# ? match-case (switch) statement:
# match age:
#     case 17:
#         print(f"{name} you are a minor.")
#     case 40:
#         print(f"{name} you are an adult.")
#     case 65:
#         print(f"{name} you are a senior citizen.")
#     case _:
#         print(f"{name} you are an alien")

# ? match-case (switch) statement:
# match age:
#     case _ if age < 18:
#         print(f"{name} you are a minor.")
#     case _ if age >= 18 and age < 60:
#         print(f"{name} you are an adult.")
#     case _:
#         print(f"{name} you are a senior citizen.")
