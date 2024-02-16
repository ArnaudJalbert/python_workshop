"""
There are 2 main types of loops in python: for loops and while loops
"""

x = 0

while x < 10:  # like the if statement, we check if a condition is true
    # like the if statement, the indentation is important
    x += 1
    print(x)

# ---------------------------------------

print("-----------------")

x = 0

while x < 10:
    # like the if statement, the indentation is important
    x += 1
print(x)  # the print only happens AFTER the loop here since it is outside the indentation

print("-----------------")

# ---------------------------------------

# break keyword allows us to exit the loop immediately
# continue keyword allows us to go directly to the next iteration of the loop

y = 0

while True:
    if y >= 10:
        break

    if y % 2 == 1:
        y += 1
        continue  # we stop here and don't run the rest of the loop code, just go straight to the next iteration

    print(f"{y} is even")

    y += 1

print("-----------------")

# ---------------------------------------

# for loops work a little differently in python
# we are used to the syntax for(let i = 0; i < array.length; i++)
# here is how we could mimic that in python

a_numbers_list = [35, 23, 73, 94, 75, 86]

# use the range function to get the indexes
a_list_range = range(0, len(a_numbers_list))
print(f"We now have the indexes: {a_list_range}")

print("-----------------")

# ---------------------------------------

for index in a_list_range:
    print(f"index: {index}")
    print(a_numbers_list[index])

# but there is a simpler way to do this...
# instead of passing the range and accessing the list by index
# we can access the variable of the list directly

for number in a_numbers_list:
    # we loop over each element in the list and assign them to "number"
    print(number)

print("-----------------")

# ---------------------------------------

# if you also need the index, we can use the enumerate function
# some functions, like enumerate, will return two values
# we can unpack them into two variables in this case
for index, number in enumerate(a_numbers_list):
    print(f"index: {index}")
    print(f"number: {number}")

print("-----------------")

# ---------------------------------------

the_dictionary = {"First": 1, "Second": 2, "Third": 3}

# to loop over dictionaries, we can use the items function
for key, value in the_dictionary.items():
    print(f"key: {key}")
    print(f"value: {value}")

print("-----------------")

# ---------------------------------------

the_string = "The string"

# we can also loop over the characters of a string
for character in the_string:
    print(f"character: {character}")

print("-----------------")

# ---------------------------------------

# EXERCISE
# From all the number in the_list_to_filter, find all the numbers
# that are greater than 50 and store them in the list "the_list_filtered"

the_list_to_filter = [65, 34, 23, 106, 34, 56, 81, 12]
the_list_filtered = []

for number in the_list_to_filter:
    if number > 50:
        the_list_filtered.append(number)

print(the_list_filtered)

print("-----------------")

# ---------------------------------------

# EXTRA EXERCISE
# From all the number in the_list_to_filter, find all the numbers
# that are greater than 50 and store them in the dictionary "the_dict_filtered"
# where the key is the index of the list where the number is and the value the actual number
# if the number is greater than 100, print "Slay"
# print the dictionary after
the_dict_filtered = {}

print("-----------------")

# ---------------------------------------
