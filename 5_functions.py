from math_package.math import a_function_AAAA

"""
functions are blocks of code that can called and re-used multiple times
we can also add parameters which can be given when they are called to make them more flexible
"""

a_function_AAAA()

# define a function with the keyword "def"
def a_simple_function():
    print("in a_simple_function")


a_simple_function()
a_simple_function()
print("-----------------")


# ---------------------------------------


# we can add parameters between the ()
def a_function_with_1_param(param):
    # param should be an integer
    print(f"in a_function_with_1_param with parameters: {param}")


a_function_with_1_param("Bonjour")
# we can pass any data types to the function
a_function_with_1_param(1)
a_function_with_1_param([1, 2, 3, 4])
print("-----------------")


# ---------------------------------------


# we can add as many parameters as we want between the ()
def a_function_with_params(day, month, year):
    print(f"in a_function_with_params with parameters: {day}, {month}, {year}")


a_function_with_params(month=8, day=1, year=2023)
print("-----------------")


# ---------------------------------------


# we can also define optional parameters
def a_function_with_optional_params(param=5, param2="Hello"):
    print(f"in a_function_with_params with parameters: {param}, {param2}")


# we can use it like before
a_function_with_optional_params("Bonjour", 1)
# we can give it just 1 argument
a_function_with_optional_params("Bonjour")
# we can give it just 0 argument
a_function_with_optional_params()
# we can specify which argument we wish to pass
a_function_with_optional_params(param2=54)
# we can mix and match
a_function_with_optional_params("Hello", param2=54)
a_function_with_optional_params(param2="alo", param="fhshs")
print("-----------------")

# ---------------------------------------

x = None


# we can add a return value to the function
def addition(x, y):
    result = x + y
    return result


an_addition = addition(5, 19)
print(an_addition)

"""
in general, a function should have on purpose
be careful when you code to not give your function multiple responsibilities
it's better to make multiple functions that each do one specific things
when you are copying and pasting code, you can probably make a function instead and avoid repetition of code
"""
