import config
import pokeDataGenerator
import json

pokedex = {}

for i in range(1, config.MAX_POKEMON_ID + 1):
    pokedex[i] = pokeDataGenerator.generate_pokemon_data(i)


print pokedex.keys()