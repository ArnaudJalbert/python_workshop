"""
before running this, we need to install pandas
just type this in your terminal: pip install pandas
"""

# use the import keyword to import modules
import pandas as pd

# we can also import our own code
import some_functions

# quick tip we can reuse the code we wrote even in different files
some_functions.a_simple_function()

# we can use the .read_csv function to load data from a csv
pokemon_data = pd.read_csv("./pokemons.csv")

# we can also read Excel files
pokemon_data_excel = pd.read_excel("pokemons.xlsx")

# we can also read any type of file, as long as we can separate the data with a character
pokemon_data_txt = pd.read_csv("./pokemons.txt", delimiter=";")
print(pokemon_data_txt)

# pandas returns us a dataframe https://www.geeksforgeeks.org/creating-a-pandas-dataframe/
# see documentation here: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
