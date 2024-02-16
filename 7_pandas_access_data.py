import pandas as pd

pokemon_data = pd.read_csv("pokemons.csv")

# seeing heads and tails
print(pokemon_data.head(10))
print(pokemon_data.tail(10))
print("-------------------")

# ---------------------------------------

print(f"columns' names of our data: {pokemon_data.columns}")
print("-------------------")

# ---------------------------------------

# we can access a certain column with:
print(pokemon_data.hp)
# or
print(pokemon_data["hp"])
# we can also include multiple columns
print(pokemon_data[["type1", "type2"]])
print("-------------------")

# ---------------------------------------

# we can also access specific rows with iloc
print(pokemon_data.iloc[5])
print("-------------------")
# we can access multipl items with iloc as well
print(pokemon_data.iloc[6:9])  # 9 is excluded in this case
print(pokemon_data.iloc[6:9][["name", "hp", "type1", "type2"]])

