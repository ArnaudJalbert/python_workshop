import pandas as pd

pokemon_data = pd.read_csv("./pokemons.csv")

# suppose we want to add a row where we have the total attack: atk+spatk
# we could do a for loop to get each one, but we can use pandas + operator instead

pokemon_data["total_atk"] = pokemon_data["atk"] + pokemon_data["spatk"]

print(pokemon_data[["name", "total_atk"]].sort_values("total_atk", ascending=False))
print(pokemon_data.columns)

# we can also use the data to make some practical operations
# for example, we can get the mean of a certain columns
mean_spdef = pokemon_data.spdef.mean()
# we can get the sum
sum_hp = pokemon_data.hp.sum()

# we can also write the new dataframe in a csv as well
pokemon_data.to_csv("total_attack.csv", index=False)

