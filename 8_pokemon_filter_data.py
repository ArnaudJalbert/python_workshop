import pandas as pd

pokemon_data = pd.read_csv("./pokemons.csv")

# we can use a for loop to iterate over a dataframe
for index, row in pokemon_data.iterrows():
    print(f"index: {index}")
    print(f"{row['name']} attack: {row.atk}")

# what if we wanted to filter data?
# we could use a for loop, but there is a much better way!

# we can use the loc function to do so!
fire_type_pokemon = pokemon_data.loc[pokemon_data["type1"] == "fire"]

water_poison_type_pokemon = pokemon_data.loc[
    (pokemon_data["type1"] == "water") & (pokemon_data["type2"] == "poison")
]

fire_and_grass_pokemon = pokemon_data.loc[
    (pokemon_data["type1"] == "fire") | (pokemon_data["type1"] == "grass")
]

print(fire_and_grass_pokemon["name"])
