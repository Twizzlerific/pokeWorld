
**_pokéWorld_** is an entity based dataset creation tool with a Pokémon twist. We generate "Pokemon Trainers" using the [Faker](https://github.com/joke2k/faker) and then assign each Trainer between 1-6 Pokemon using data sourced from [Veekun's Pokedex](https://github.com/veekun/pokedex).
This becomes the foundation for a variety of performance tests, component training, ML workloads, and more!

![pokeworld](docs/assets/pokeworld.png)


# Getting Started
With version 1.1, the process starts by editing the configuration file configs/configuration.py to decide the number of new rows to create under `TRAINER_COUNT` as well as the `OUTPUT_METHOD` to determine how the script will format the data and where it will send the records. 

Depending on the desired output, we may need to create the tables first. Use the CREATE statement in the [Tables Guide](docs/working_with_tables.md) to create the tables in the various components. 

### First Run:

1: Configure pokeWorld:
```bash
vi configs/configuration.py
OUTPUT_METHOD   = 'CSV'
OUTPUT_TO_FILE  = 'True'
TRAINER_COUNT   = 3
```

> Fore more information on Configuring the Generator see [Configuration Guide](docs/configuration.md)


2:  Install requirements: 
``` bash
# pip install -r requirements.txt
```


3: Run script:
``` bash
# python pokeWorld.py
```

Files should output to the output directory. To run in the background, `nohup` can be used. To run multiple generators at a time run using:

`nohup python pokeWorld.py &`

The script should randomly generate user data, format the data, and (if specified via the configuration) connect to the necessary servers to upload the data. 

---
__Credits__
- [Faker](https://github.com/joke2k/faker)
- [Veekun's Pokedex](https://github.com/veekun/pokedex)
- [Nintendo](https://www.nintendo.com/)

__DISCLAIMER:__
Pokemon is the intellectual property of Nintendo and GAME FREAK. The author assumes no right to this data and the use is purely for education. 