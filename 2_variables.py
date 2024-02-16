"""
Unlike other programming languages, you do not have
to declare the type of the variable and there are
no special keywords to sue to declare a variable
"""

# there are still different data types

# integer -> ...,-2, -1, 0, 1, 2, 3,...
integer_example = 10
print("integer_example is a", type(integer_example))
print("-------------------")

# string -> any combination of characters
string_example = "Hello World!"
print("string_example is a", type(string_example))
print("-------------------")

# float -> any decimal number
float_example = 14.723
# if we want a "rounded" float, we can add . at the end
another_float_example = 14.
print("float_example is a", type(float_example), " and its value is ", float_example)
print("another_float_example is a", type(another_float_example), " and its value is ", another_float_example)
print("-------------------")

# boolean -> True or False
# note that True and False need upper cases on the first letter
true_example = True
false_example = False
print("true_example is a", type(true_example))
print("false_example is a", type(false_example))
print("-------------------")

# list -> collection of any data types
# we can put any data type in a list
# we can also mix and match with different data types
# declare it with [,]
list_example = ["first_element", integer_example, float_example, string_example, false_example]
print("list_example is a ", type(list_example))
print("the list contains: ", list_example)
print("-------------------")

# to add an element to the end of the list we can use the "append" function
list_example.append("last_element")
print("list_example with the added element", list_example)
print("-------------------")

# we can access a list by index, the first index is always 0
print("the first element of list_example is", list_example[0])
# we can find the length of a list with len()
list_example_length = len(list_example)
print("the length of list_example is", list_example_length)
# to access the last element, we can use the length and remove 1 since the first element is 0
print("the last element of list_example is", list_example[list_example_length-1])
# we can also use negative index to access the list "backwards
# the index -1 is the last element, -2 is the second to last element
print("the second to last element of list_example is", list_example[-2])
print("-------------------")

# a dictionary is a key/value pair data type
# similar to the object in javascript and the HashMap in Java
# declare it with {Key: Value}
dictionary_example = {"First": 1, "Second": "Allo", "Third": 3}
print("dictionary_example content:", dictionary_example)
# access the element with the key value
print("element with 'Second' key is", dictionary_example["Second"])
# add an element with the [] syntax
dictionary_example["Fourth"] = 4
print(dictionary_example)
print(dictionary_example.values())
print("element with 'Fourth' key is", dictionary_example["Fourth"])
print("-------------------")

# to convert data type, we can use the str, int and float
converted_int_to_float = float(integer_example)
print("converted_int_to_float is a", type(converted_int_to_float), "the new value is", converted_int_to_float)
converted_string_to_int = int("5")
print("converted_string_to_int is a", type(converted_string_to_int), "the new value is", converted_string_to_int)
converted_int_to_string = str(integer_example)
print("converted_int_to_string is a", type(converted_int_to_string), "the new value is", converted_int_to_string)
x = "5"
y = int(x)
print(type(y))
print("-------------------")

# use f string to easily print the content of variable
name = "Arnaud"
last_name = "Jalbert"
age = 24
print(f"My name is {name} and my last name is {last_name} and I am {age} years old.")





