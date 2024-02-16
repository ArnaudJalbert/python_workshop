"""
now that we can assign variables, we can
start checking equality between them
"""

# the if statement can be used to execute
# a block of code only if the condition is true
# we can use == to check the equality between two values

if True:  # the if statement needs the : after its declaration
    print("It is true")
    print("hello")
else:
    print("It is False")

if False:
    print("It is true")
else:
    # unlike other languages, the indentation will impact the code
    # but there are no parentheses to worry about
    print("It is False")
print("-------------------")

# ---------------------------------------

x = 10
y = 10

if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")

y = 8

if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}!!!!!!!!!")

# ---------------------------------------

# example of non-indented statement
if x == y:
    print("Passing by....")
print(f"{x} is equal to {y}(not really... need to be careful with the indentation)")
print("-------------------")

# ---------------------------------------

# we can also check multiple conditions within the same if statement with 'and' or 'or'
if x == y or x < y:
    print(f"{x} is less than or equal to {y}")
else:
    print(f"{x} is greater than {y}")
print("-------------------")

a = 5
b = 2

# ---------------------------------------

# we can use elif to check other conditions if the first 'if' is false
# if one elif is true, the other will not be checked
# equivalent to "else if" in other languages
if y <= x and a == b:
    print(f"{x} is equal to {y}")
elif y > x and a > b:
    print(f"{y} is greater than {x} and {a} is greater than {b}")
elif True:
    print(f"{y} is greater than {x}")
print("-------------------")

# ---------------------------------------

# to check if a certain element is in a list,
# no need to make a loop, we can simply use the "in" keyword

the_list = [1, 2, 3, 4, 5, 6]

if 5 in the_list:
    print("5 is in the list")
if 7 in the_list:
    print("7 is in the list")
else:
    print("7 is not in the list")

# we can also use "in" for string
# it can check if a certain substring is in the string
the_string = "Hello World!"
if "world" in the_string.lower():
    print("World is in the string")

if "Bonjour" in the_string:
    print("Bonjour is in the string")
else:
    print("Bonjour is not in the string")
print("-------------------")

# ---------------------------------------
# same thing for the dictionaries
# by default, it will only check the keys
the_dictionary = {"First": 1, "Second": 2, "Third": 3}

if "First" in the_dictionary:
    print("First is in the keys")

# to check the values, use .values()
if 2 in the_dictionary.values():
    print("2 is in the values")
print("-------------------")


# ---------------------------------------
