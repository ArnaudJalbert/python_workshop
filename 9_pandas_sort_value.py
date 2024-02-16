import pandas as pd

pokemon_data = pd.read_csv("./pokemons.csv")

# we can sort the data from a certain column
pokemon_sort_by_hp = pokemon_data.sort_values("hp", ascending=True)

print(pokemon_sort_by_hp[["name", "hp"]])

# we can sort the data from multiple columns
pokemon_sort_by_def_and_type = pokemon_data.sort_values(["def", "type1"], ascending=[False, True])

print(pokemon_sort_by_def_and_type[["name", "def", "type1"]].head(12))